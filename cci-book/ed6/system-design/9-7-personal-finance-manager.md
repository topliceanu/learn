# 9.7 Personal finance manager

1. Problem exploration
- Who are our users? Are they individuals or businesses?
- What do we want to achive with our recommendations? Help users spend less? Lead a healthier life? What to buy next? What to stop buying?
- Numbers: how many users? how many banks? how large is the purchase history of every user? How many recommendations
- How do we interract with banks? Crawl html or API? Are they partners in this or it's just us using them?
- How do we deliver recommendations? Through a website? Through an app? through email? Are they real-time?
- Any other input sources? Can users tag transactions or add cache transactions manually? Can users create their own tags?
  Can we add location data from a phone?
Assumptions:
- I'll assume there are far fewer banks than users, maybe ~100 banks and 100m users
- I'll assume each user does 10 transactions a day on average.
- I'll assume we need to transfer recs in an app and on a weekly newsletter.
No real-time recs, we can calculate them offline every day and once a week.

2. High level architecture
```
                +-----+
                |Queue|       +----+
                +-^-|-+    +--|Bank|
+--+    +--+    +-|-V---+  |  +----+
|FE|<---|DB|<---|Crawler|<-+
+--+    +^-+    +-------+  |  +----+
         |                 +--|Bank|
   +-----+-----+              +----+
   |Recommender|
   +-----------+
```
3. Solution breakdown

Contracts:
- banks give us back `list purchase`, where `type purchase = { what string, labels list label, timestamp date, amount int }`
- crawler aggregates these thing per user `type updates = { user_id int, purchases list purchase }`
- recommender: ???
- the system is write heavy, a tipical user does a few transactions a day, but will check recommendations on average once a month or through an email alert.
- transactions are independent and read-only, including any meta-data that we may assign to it, like tags.
- we can use this to decide on the storage engine: block storage - each user/month is a
file with appended transactions one per row. Older files get archived, even older archives get shipped to cold storage.
We need an abstraction on top of these storage implementations.

Options:
- recommender could have it's own storage and FE with query the rec dirrectly to get recommendations.
- we need to shard! By user, by bank or by seller: by bank - what if we have very popular banks; by user - how do we reshuffle user to avoid hot shards?
- some banks can offer a read-only API or we need to crawl them (this is much more expensive)
- cralwer can be generic - perform all crawling; or dedicated cralwer boxes for specific banks - it will help spread the load better if some bank's pages load slowly.
- we can have different frequencies depending on how active users are.

4. Focus on a specific component.
- the main component is the recommender. All other things are well defined and understood.
- the FE is stateless, solutions to make it scale are well understood.
- the crawler is also stateless, so it only needs a queue in front to spread the load.
- I believe the value producing component here is the Recommender
    - it needs to be async, running a batch job every day or every week, consuming data for a user and producing recs.
    - it can have it's own storage, in this case, the crawler will deposit the spending data in the cralwer's storage, say a document database.
    - likewise the FE can talk to the rec dirrectly

5. Identify key Issues:
- assigning tags to transactions might be error prone
- recommender getting slower and slower
- real-time recommendations? we would need to get in
