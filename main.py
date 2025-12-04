# Final Code for Project Submission: AI Dynamic Skill Finder (Remote Jobs Only)

import urllib.request
import json
import re
import collections

# --- 1. STOP WORDS / FILTER (শব্দ বাদ দেওয়ার তালিকা) ---
STOP_WORDS = {
    "and", "the", "to", "of", "in", "for", "with", "a", "an", "is", "are",
    "on", "at", "be", "we", "our", "you", "your", "will", "can", "have",
    "has", "as", "or", "that", "this", "from", "by", "it", "job", "work",
    "team", "experience", "skills", "working", "knowledge", "years", "role",
    "looking", "opportunity", "company", "business", "support", "please",
    "strong", "time", "new", "remote", "full", "part", "requirements",
    "description", "about", "application", "using", "must", "join", "us",
    "amp", "per", "who", "what", "high", "world", "pages", "internal",
    "build", "building", "needs", "responsibilities", "ensure", "daily",
    "make", "able", "etc", "get", "like", "use", "best", "day", "senior",
    "positions", "opportunities", "first", "implement", "design", "team",
    "engineer", "solutions", "environment", "global", "across", "end", "level",
    "systems", "product", "technology", "development", "maintenance", "client"
}

# --- 2. OUTPUT VISUALIZATION FUNCTION (গ্রাফ তৈরি) ---
def create_bar(percentage):
    # ASCII বারটি 100% এ ক্যাপ করা হয়েছে
    visual_percentage = min(percentage, 100) 
    hashes = int(visual_percentage / 10)
    bar = '#' * hashes + ' ' * (10 - hashes)
    return f"[{bar}]"

# --- 3. DATA FETCHING (লাইভ ডেটা আনা) ---
def get_jobs(query):
    clean_query = query.replace(" ", "+")
    url = f"https://remotive.com/api/remote-jobs?search={clean_query}"
    source_name = "Remote Job API (Remotive)"
    jobs = []
    
    print(f"\nSearching '{source_name}' for '{query}' jobs...")
    
    try:
        req = urllib.request.Request(
            url, data=None, headers={'User-Agent': 'Mozilla/5.0'}
        )
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode())
        
        for job in data.get('jobs', []):
            jobs.append({'title': job.get('title', ''), 'description': job.get('description', '')})
            
        print(f"Success! Downloaded {len(jobs)} real job postings from {source_name}.")
        return jobs
    except Exception as e:
        print(f"Connection Error: {e}")
        return []

# --- 4. CORE ANALYSIS FUNCTION ---
def extract_trending_skills(jobs):
    print(f"Analyzing {len(jobs)} job advertisements to find top skills...")
    all_words = []
    
    for job in jobs:
        text = job.get('title', '') + " " + job.get('description', '')
        
        clean_text = re.sub('<[^<]+?>', '', text).lower()
        words = re.findall(r'\b[a-z]{3,15}\b', clean_text)
        
        meaningful_words = [w for w in words if w not in STOP_WORDS]
        all_words.extend(meaningful_words)
        
    word_counts = collections.Counter(all_words)
    return word_counts.most_common(20)

# --- 5. EXECUTION BLOCK ---
if __name__ == "__main__":
    print("--- AI DYNAMIC SKILL FINDER: REMOTE JOBS ONLY ---")
    
    user_search = input("\nEnter your desired REMOTE job category (e.g., 'Cloud Engineer', 'DevOps', 'Data Science'): ")
    
    if user_search:
        jobs = get_jobs(user_search)
        
        if len(jobs) > 0:
            top_skills = extract_trending_skills(jobs)
            total_jobs = len(jobs)

            # চূড়ান্ত আউটপুট ফরমেট
            print("\n" + "="*80)
            print(f"📈 DETAILED SKILL REPORT FOR REMOTE '{user_search.upper()}' (Analyzed {total_jobs} Jobs)")
            print("="*80)
            print(f"{'RANK':<5}{'SKILL / TOOL':<18}{'DEMAND VISUALIZATION':<15}{'MENTIONS':<10}{'FREQUENCY'}")
            print("-" * 80)
            
            for rank, (word, count) in enumerate(top_skills, 1):
                percentage = (count / total_jobs) * 100 
                bar_viz = create_bar(percentage)
                
                print(f"{rank:4}. {word.upper():<16} {bar_viz:<15} {count:<10} {percentage:.1f}%")
                
            print("-" * 80)
            print("✅ Suggestion: Skills with the highest frequency are critical for this job market.")
        else:
            print("No remote jobs found for this keyword. Try a broader term.")
    else:
        print("Please enter a valid keyword.")