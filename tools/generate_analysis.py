import json
import os
import tempfile
import requests
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def download_pdf(arxiv_id: str, temp_dir: str) -> str | None:
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    pdf_path = os.path.join(temp_dir, f"{arxiv_id}.pdf")

    try:
        response = requests.get(pdf_url, timeout=30)
        response.raise_for_status()

        with open(pdf_path, 'wb') as f:
            f.write(response.content)

        return pdf_path
    except Exception as e:
        print(f"    Failed to download {arxiv_id}: {e}")
        return None


def extract_pdf_content(pdf_path: str) -> str | None:
    try:
        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()

        pdf_part = types.Part.from_bytes(data=pdf_data, mime_type="application/pdf")

        response = gemini_client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=[
                pdf_part,
                """Extract the full text content from this paper, focusing especially on:
1. Introduction and motivation
2. Method/approach details
3. Experimental setup and results
4. Discussion section
5. Limitations section
6. Conclusion and future work

Provide the extracted text in a structured format."""
            ]
        )

        return response.text
    except Exception as e:
        print(f"    Failed to extract content: {e}")
        return None


def generate_analysis(paper_content: str, paper_title: str) -> str | None:
    try:
        prompt = f"""You are a critical AI/robotics researcher analyzing the paper "{paper_title}".

Based on the paper content below, provide a sharp, insightful analysis covering:

1. **Novel Techniques**: What new methods or approaches does this paper introduce?
2. **Strengths**: What is particularly impressive or well-executed?
3. **Weaknesses**: What could be improved? Are there experimental gaps, limited baselines, insufficient training, or methodological issues?
4. **Impact**: How significant is this work for the field?

Be direct and technical. Point out both what's cool and what's lacking. Keep it concise (300-400 words).

Paper content:
{paper_content[:15000]}
"""

        response = gemini_client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )

        return response.text
    except Exception as e:
        print(f"    Failed to generate analysis: {e}")
        return None


def generate_future_directions(paper_content: str, paper_title: str) -> list[str]:
    try:
        prompt = f"""You are a forward-thinking AI/robotics researcher analyzing the paper "{paper_title}".

Based on the paper's conclusion, discussion, and limitations sections, suggest 3-5 concrete future experiments or research directions.

For EACH direction, provide:
1. **What to explore**: The specific problem or limitation to address
2. **How to achieve it**: Concrete technical approach (e.g., architectural changes, new loss functions, different datasets)

Focus on actionable, technically specific suggestions. Examples:
- "Handle multi-image observations by modifying the transformer to accept multiple embedded images with temporal attention"
- "Address sim-to-real gap by incorporating domain randomization with learned domain classifiers"
- "Improve data efficiency by integrating self-supervised pre-training on unlabeled robot videos"

Paper content (especially conclusion/limitations):
{paper_content[-10000:]}

Return as a JSON array of strings, where each string is one direction with format:
"**[Direction Name]**: [Problem to solve]. *Approach*: [Specific technical method]"
"""

        response = gemini_client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )

        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:]
        if text.endswith('```'):
            text = text[:-3]
        text = text.strip()

        try:
            directions = json.loads(text)
            return directions if isinstance(directions, list) else []
        except:
            lines = [line.strip() for line in text.split('\n') if line.strip() and not line.strip().startswith('[') and not line.strip().startswith(']')]
            cleaned = [line.strip('",') for line in lines if line.strip('",')]
            return cleaned[:5]
    except Exception as e:
        print(f"    Failed to generate future directions: {e}")
        return []


def generate_paper_analysis(paper: dict, temp_dir: str) -> tuple[str | None, list[str]]:
    arxiv_id = paper['arxiv']['arxiv_id'].split('v')[0]
    title = paper['arxiv']['title']

    print(f"  Downloading PDF for {arxiv_id}...")
    pdf_path = download_pdf(arxiv_id, temp_dir)

    if not pdf_path:
        return None, []

    print(f"  Extracting content...")
    content = extract_pdf_content(pdf_path)

    if not content:
        return None, []

    print(f"  Generating analysis...")
    analysis = generate_analysis(content, title)

    print(f"  Generating future directions...")
    directions = generate_future_directions(content, title)

    return analysis, directions


def generate_all_analyses(papers_file: Path):
    with open(papers_file, 'r') as f:
        papers = json.load(f)

    print(f"Generating analysis for {len(papers)} papers...\n")

    with tempfile.TemporaryDirectory() as temp_dir:
        for i, paper in enumerate(papers, 1):
            arxiv_id = paper['arxiv']['arxiv_id'].split('v')[0]
            title = paper['arxiv']['title'][:60]

            if paper.get('gemini_analysis') and paper.get('future_directions'):
                print(f"[{i}/{len(papers)}] {arxiv_id} - {title}...")
                print(f"  ✓ Already has analysis, skipping")
                continue

            print(f"[{i}/{len(papers)}] {arxiv_id} - {title}...")

            analysis, directions = generate_paper_analysis(paper, temp_dir)

            if analysis:
                paper['gemini_analysis'] = analysis
                print(f"  ✓ Analysis generated ({len(analysis)} chars)")

            if directions:
                paper['future_directions'] = directions
                print(f"  ✓ {len(directions)} future directions generated")

            with open(papers_file, 'w') as f:
                json.dump(papers, f, indent=2)

            print()

    print(f"\n✅ Generated analysis for {len(papers)} papers!")


if __name__ == "__main__":
    papers_file = Path(__file__).parent.parent / "data" / "papers.json"
    generate_all_analyses(papers_file)
