import os
import requests
import time
from dotenv import load_dotenv
from schemas import TwitterMetrics

load_dotenv()


def extract_tweet_id_from_url(twitter_url: str) -> str:
    if "status/" in twitter_url:
        return twitter_url.split("status/")[-1].split("?")[0].strip()
    elif "x.com" in twitter_url:
        parts = twitter_url.split("/")
        for i, part in enumerate(parts):
            if part == "status" and i + 1 < len(parts):
                return parts[i + 1].split("?")[0].strip()
    return twitter_url.strip()


def fetch_twitter_metrics_batch(tweet_data: list[tuple[str, str]], max_retries: int = 3) -> dict[str, TwitterMetrics]:
    if not tweet_data:
        return {}

    token = os.getenv("TWITTER_BEARER_TOKEN")
    if not token:
        print("Twitter API error: TWITTER_BEARER_TOKEN not found in .env")
        return {url: TwitterMetrics(tweet_url=url, tweet_id=tid) for url, tid in tweet_data}

    headers = {
        "Authorization": f"Bearer {token.strip()}"
    }

    tweet_ids = [tid for _, tid in tweet_data]
    url_by_id = {tid: url for url, tid in tweet_data}

    params = {
        "ids": ",".join(tweet_ids),
        "tweet.fields": "public_metrics,created_at"
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(
                "https://api.x.com/2/tweets",
                headers=headers,
                params=params,
                timeout=10
            )

            if response.status_code == 200:
                data_list = response.json().get("data", [])
                results = {}

                for data in data_list:
                    tweet_id = data["id"]
                    metrics = data.get("public_metrics", {})
                    tweet_url = url_by_id[tweet_id]

                    results[tweet_url] = TwitterMetrics(
                        tweet_url=tweet_url,
                        tweet_id=tweet_id,
                        likes=metrics.get("like_count"),
                        retweets=metrics.get("retweet_count"),
                        replies=metrics.get("reply_count"),
                        quotes=metrics.get("quote_count"),
                        views=metrics.get("impression_count")
                    )

                for url, tid in tweet_data:
                    if url not in results:
                        results[url] = TwitterMetrics(tweet_url=url, tweet_id=tid)

                return results

            elif response.status_code == 429:
                wait_time = (2 ** attempt) * 5
                print(f"Rate limited. Waiting {wait_time}s before retry {attempt + 1}/{max_retries}...")
                time.sleep(wait_time)
                continue

            else:
                print(f"Twitter API error: {response.status_code} - {response.text}")
                return {url: TwitterMetrics(tweet_url=url, tweet_id=tid) for url, tid in tweet_data}

        except Exception as e:
            print(f"Twitter API exception: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue

    return {url: TwitterMetrics(tweet_url=url, tweet_id=tid) for url, tid in tweet_data}


def fetch_twitter_metrics(twitter_url: str, max_retries: int = 3) -> TwitterMetrics:
    if not twitter_url:
        return TwitterMetrics()

    tweet_id = extract_tweet_id_from_url(twitter_url)
    result = fetch_twitter_metrics_batch([(twitter_url, tweet_id)], max_retries)
    return result.get(twitter_url, TwitterMetrics(tweet_url=twitter_url, tweet_id=tweet_id))


if __name__ == "__main__":
    test_tweets = [
        "https://x.com/chichengcc/status/1758539728444629158",
        "https://x.com/moo_jin_kim/status/1801548441102991771",
        "https://x.com/irmakkguzey/status/1913276064287305730"
    ]

    print("Testing Twitter API tracker (batch mode)...\n")

    tweet_data = [(url, extract_tweet_id_from_url(url)) for url in test_tweets]
    results = fetch_twitter_metrics_batch(tweet_data)

    for tweet_url in test_tweets:
        metrics = results.get(tweet_url, TwitterMetrics())
        print(f"Tweet: {tweet_url}")
        print(f"  Likes: {metrics.likes}")
        print(f"  Retweets: {metrics.retweets}")
        print(f"  Views: {metrics.views}")
        print(f"  Replies: {metrics.replies}")
        print()
