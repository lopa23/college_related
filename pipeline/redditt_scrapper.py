import json
import time
import requests

def export_collegeresults_to_markdown(target_count=100, output_filename="admissions_100_profiles.md"):
    """
    Crawls public submissions from r/collegeresults via public JSON endpoints,
    filters for actual profiles, and compiles them into a clean Markdown document.
    """
    headers = {"User-Agent": "AdmissionsDataPipeline/2.0 (Research Archive Script)"}
    base_url = "https://www.reddit.com/r/collegeresults/hot.json"
    after = None
    profiles = []

    print(f"Collecting {target_count}+ profiles from r/collegeresults...")

    while len(profiles) < target_count:
        url = f"{base_url}?limit=100"
        if after:
            url += f"&after={after}"

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            break

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            break

        for post in posts:
            pdata = post.get("data", {})
            body = pdata.get("selftext", "")

            # Filter for standard r/collegeresults template fields
            has_stats = any(term in body.lower() for term in ["gpa", "sat", "act"])
            has_outcomes = any(term in body.lower() for term in ["accept", "reject", "decision"])
            is_valid_length = len(body) > 250

            if has_stats and has_outcomes and is_valid_length:
                profiles.append({
                    "id": len(profiles) + 1,
                    "title": pdata.get("title", "Untitled Outcome").strip(),
                    "url": f"https://reddit.com{pdata.get('permalink')}",
                    "author": pdata.get("author", "anonymous"),
                    "ups": pdata.get("score", 0),
                    "body": body.strip()
                })

            if len(profiles) >= target_count:
                break

        after = data.get("after")
        if not after:
            break
            
        time.sleep(1.2)  # Polite crawl delay

    # Write formatted Markdown file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("# Archive of 100+ College Admissions Profiles\n")
        f.write(f"*Extracted from r/collegeresults ({len(profiles)} total records)*\n\n---\n\n")
        
        # Summary index
        f.write("## Index of Profiles\n\n")
        f.write("| # | Title | Upvotes | Direct Thread |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for p in profiles:
            clean_title = p['title'].replace('|', '/')
            f.write(f"| **{p['id']:03d}** | {clean_title} | {p['ups']} | [Reddit Link]({p['url']}) |\n")
        
        f.write("\n---\n\n## Detailed Profile Submissions\n\n")

        # Full markdown posts
        for p in profiles:
            f.write(f"### Profile #{p['id']:03d}: [{p['title']}]({p['url']})\n")
            f.write(f"- **Author:** `u/{p['author']}`\n")
            f.write(f"- **Score:** {p['ups']} upvotes\n\n")
            f.write("```text\n")
            f.write(p['body'])
            f.write("\n```\n\n---\n\n")

    print(f"Complete. {len(profiles)} profiles exported to '{output_filename}'.")

if __name__ == "__main__":
    export_collegeresults_to_markdown(target_count=100)