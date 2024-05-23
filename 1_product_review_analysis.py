# Task 1 keyword highlighter

def review_replace(python_reviews):
    replace_words = ["good", "excellent", "bad", "poor", "average"]
    new_reviews =[]
    for reviews in python_reviews:
        for word in replace_words:
            reviews = reviews.replace(word, word.upper())
        new_reviews.append(reviews)
    new_reviews[3] = new_reviews[3].replace("poor".title(), "poor".upper())        
    print(*new_reviews, sep= "\n")

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
review_replace(python_reviews)

# replace_words = ["good", "excellent", "bad", "poor", "average"]
# new_reviews =[]
# for reviews in python_reviews:
#     for word in replace_words:
#         reviews = reviews.replace(word, word.upper())
#     new_reviews.append(reviews)
# print(*new_reviews, sep= "\n")

# for reviews in python_reviews:
#     reviews = reviews.lower()
#     #print(reviews.find("good")) #good is character 23 of index 0
#     #print(reviews.find("excellent")) #excellent is character 35 of index 1
#     #print(reviews.find("bad")) #bad is character 8 of index 2
#     #print(reviews.find("poor")) #poor is character 0 of index 3
#     #print(reviews.find("average")) #average is character 16 of index 4
# new_reviews =[]    
# new_reviews.append(python_reviews[0].replace("good", "good".upper()))
# new_reviews.append(python_reviews[1].replace("excellent", "excellent".upper()))
# new_reviews.append(python_reviews[2].replace("bad", "bad".upper()))
# new_reviews.append(python_reviews[3].replace("poor".title(), "poor".upper())) #Had to modify this code to search and replace titlecase poor because it's first word of sentence
# new_reviews.append(python_reviews[4].replace("average", "average".upper()))

# print(*new_reviews, sep="\n")

'''
I built a for loop that I progressively commented out to search for each word we were highlighting in the reviews.
The reason I ultimately commented out nearly the entire loop was to keep the terminal clean for users once
the replacement process actually began. To do the replacement process I new I would need
to populate a new list as python string is immutable. Once I created a new list I appended each new review
with the properly highlighted word via the .replace() and .upper() methods. I also used the .title() method when
searching for "poor" to catch that it was the first word of it's review. Lastly I printed the new list
using thr print print(*list, sep = "\n\") method to remove the brackets and separate each item by a new line.
'''

#Task 2 Sentiment Tally

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def positive_word_tally(reviews_to_tally):    
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    pos_word_count = 0
    for review in reviews_to_tally:
        for word in positive_words:
            pos_word_count += review.count(word)
    return pos_word_count

def negative_word_tally(reviews_to_tally):
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    neg_word_count = 0
    for review in reviews_to_tally:
        review = review.lower()
        for word in negative_words:
            neg_word_count += review.count(word)
    return neg_word_count
    
print(positive_word_tally(python_reviews))
print(negative_word_tally(python_reviews))

#Task 3 30 character summary
#Implement a script that takes the first 30 characters of a review 
#and appends "…" to create a summary. Ensure that the summary does not cut off in the
# middle of a word.

def review_summary(python_reviews):
    review_summaries = []
    for review in python_reviews:
        if len(review) > 30:
            last_space = review[:30].rfind(' ')
            if last_space == -1:
                summary = review[:30] + "..."
            else:
                summary = review[:last_space] + "..."
        else: 
            summary = review
        review_summaries.append(summary)
    print("A summary of the reviews:")
    print(*review_summaries, sep='\n')
review_summary(python_reviews)

'''
In line 80 I set up and defined a function to summarize the reviews in approximately 30 characters, without cutting words off.
Line 81 set up an empty list we will append the summaries too. Line 82 created a for loop that starst the program by
looping through each review in any set we feed to the function. Line 83, 89, and 90 tests 
if the review is over 30 characters and if it is not, assigns it to a summary variable is looped into a list, after a "..." is concantenated.
Line 84 assigns an integer to the variable last_space that says where the last " " is in the first 30 characters of each review
Line 85-86 is a nested if/else where the first 30 characters and the ellipses are also assigned to summary if there aren't any " " for whatever reaon found.
Line 87-88 assigns reviews sliced up until the integer value returned in last_space where the last " " will be found to the summary list that is being created by the loop and adds
the ellipses. By line 91 all 5 reviews have been concantenated with an ellipses and summarized and are appended to the empty list we created at the start
of the function. In line 92 and 93 we format the printing of this list to give a small introduction, remove the brackets and populate each list into its own terminal line.
In line 94 I call the function with our reviews.
'''