# One-Page Summary: MovieLens Genre Rating Analysis

**Name:** Namig Amrah  
**Course:** Data Analysis with CERN Open Data  
**Date:** May 2025  

---

## 1. Problem & Motivation  
Streaming platforms thrive when they know which genres users love most.  
> **Question:** Which movie genres have the highest average user rating?  

Understanding this helps services prioritize content, tailor marketing, and improve recommendations.

---

## 2. Data & Methods  
- **Dataset:** MovieLens “latest-small” (100 836 ratings, 9 742 movies)  
- **Tools:** Python (pandas, matplotlib) in Google Colab; GitHub for versioning  

**Process:**  
1. Downloaded and unzipped `ml-latest-small.zip`.  
2. Loaded `ratings.csv` & `movies.csv` in pandas.  
3. Filled missing genres with `""`, split pipe-separated genres into rows.  
4. Merged movies ↔ ratings on `movieId`.  
5. Computed mean rating per genre and took the top 10.

---

## 3. Key Finding  
The top five genres by average rating are:  
1. Romance (~3.98)  
2. Documentary (~3.90)  
3. Drama (~3.88)  
4. Musical (~3.87)  
5. Mystery (~3.85)  

---

## 4. Reflection & Next Steps  
**Learned:** data cleaning in pandas, grouping & aggregation, clear plotting.  
**Challenges:** handling list-explosion of genres, reproducibility via Colab→GitHub.  
**Next:** weight by number of ratings, explore user demographics, apply ML for recommendations.

---

**Repo & Files:**  
- `analysis.ipynb` – code & process  
- `avg_rating_by_genre.png` – chart of top genres  
- `one_page_summary.md` – this summary  
