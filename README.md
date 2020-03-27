# Genre-Classification-NLP
## Inspiration/Goals
You hear many people say how genres are just labels and that in reality, music has no boundaries. But we wanted to see if genres can say more about their respective communities in terms of language. So the  goal of this project was to investigate the differences between 4 genres (Rock, Pop, Hip-Hop, and Country) by analyzing the lyrics using Natural Language Processing.

## Dataset
We found our dataset from Kaggle that consisted of over 380,000 songs plus lyrics. 

### Data Cleaning
Data cleaning consisted of removing all song that were tagged with multiple genres, removing songs with no lyrics, removing stop words, and dealing with class imbalance

### Exploratory Data Analysis

   -Words Counts by genre
    -Hip-Hop stood out from the other 3 genres in both unique words and average word length
        
![](/Images/avg_words_per_genre.png) ![](/Images/uniquewords_genre.png)
        
  
  -Words Clouds shows overlap between all 4 genres but with a few keys differences:
    -Country: Night, Day; Pop: Baby, Feel; Hip-Hop: lots of slang and explicit lyrics
        
Top 25 Country Words ![](/Images/top_25_country.png) Top 25 Pop Words![](/Images/top_25_pop.png) 
Top 25 Rap Words ![](/Images/top_25_rap.png) Top 25 Rock Words ![](/Images/rock.png)

        
## Modeling
After running several models including Naive Bayes, SGD, Logistic Regression, and XGBoost,
our best F1 score of .751 was accomplished using XGBoost without upsampling. We did try applying an upsampled dataset to XGBoost to see if that improved the score, however, upsampling resulted in a worse score of .51. Even though the two models had drastically different results, both had similar performance of predicting Pop songs.

## Conclusion/Final Insights

    - Pop songs are easier to predict with lyrics
    - Additional features are needed to precisely predict other genres
    - Model could possibly be improved using word embedding to give lyrics more context

        
