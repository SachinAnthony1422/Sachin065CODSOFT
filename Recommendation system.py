import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Sample movie data
movies = {
    'movie_id': [1, 2, 3, 4, 5, 6, 7],
    'title': ["The Avengers", "Comedy Central", "Mad Max", "The Shawshank Redemption", "Superbad", "Die Hard", "The Godfather"],
    'genre': ["Action", "Comedy", "Action", "Drama", "Comedy", "Action", "Drama"]
}

# Initialize dataframes
movies_df = pd.DataFrame(movies)
ratings_df = pd.DataFrame(columns=['user_id', 'movie_id', 'rating'])

# Content-based filtering function
def recommend_movies(user_id, n=3):
    # Get user's rated movies
    user_ratings = ratings_df[ratings_df['user_id'] == user_id]
    user_movies = user_ratings.merge(movies_df, on='movie_id')
    
    if user_movies.empty:
        return "No recommendations available. Please rate some movies first."
    
    # Get the genres of the movies the user has rated
    genres = user_movies['genre'].value_counts().index.tolist()
    
    # Recommend movies based on genres
    recommendations = movies_df[movies_df['genre'].isin(genres)]
    recommendations = recommendations[~recommendations['movie_id'].isin(user_movies['movie_id'])]
    
    if recommendations.empty:
        return "No new recommendations available."
    
    rec_list = recommendations.head(n)
    rec_text = f"Recommendations for User {user_id}:\n"
    for _, row in rec_list.iterrows():
        rec_text += f"  {row['title']} ({row['genre']})\n"
    
    return rec_text

def add_rating(user_id, movie_id, rating):
    global ratings_df
    # Check if the movie_id and user_id are valid
    if movie_id not in movies_df['movie_id'].values:
        return "Invalid movie ID."
    
    new_rating = pd.DataFrame({
        'user_id': [user_id],
        'movie_id': [movie_id],
        'rating': [rating]
    })
    
    global ratings_df
    ratings_df = pd.concat([ratings_df, new_rating], ignore_index=True)
    return "Rating added successfully."

# GUI Setup
def show_recommendations():
    try:
        user_id = int(user_id_entry.get())
        recommendations = recommend_movies(user_id)
        messagebox.showinfo("Recommendations", recommendations)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid user ID")

def submit_rating():
    try:
        user_id = int(user_id_entry.get())
        movie_id = int(movie_id_entry.get())
        rating = int(rating_entry.get())
        response = add_rating(user_id, movie_id, rating)
        messagebox.showinfo("Response", response)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for user ID, movie ID, and rating")

# Set up the GUI
root = tk.Tk()
root.title("Movie Recommendation System")

tk.Label(root, text="Enter User ID:").grid(row=0, column=0, padx=10, pady=10)
user_id_entry = tk.Entry(root)
user_id_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Movie ID:").grid(row=1, column=0, padx=10, pady=10)
movie_id_entry = tk.Entry(root)
movie_id_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Enter Rating (1-5):").grid(row=2, column=0, padx=10, pady=10)
rating_entry = tk.Entry(root)
rating_entry.grid(row=2, column=1, padx=10, pady=10)

recommend_button = tk.Button(root, text="Get Recommendations", command=show_recommendations)
recommend_button.grid(row=4, columnspan=2, pady=10)

add_rating_button = tk.Button(root, text="Add Rating", command=submit_rating)
add_rating_button.grid(row=5, columnspan=2, pady=10)

root.mainloop()
