
from flask import Blueprint, render_template, request, jsonify, redirect, url_for,session
import openai
import random
import time
import os
import re

views = Blueprint(__name__,'views')

api_key = os.getenv('api_key')

def delete_sessions():
    for key in list(session.keys()):
        del session[key]
        
@views.route('/category')
def get_category():
    if 'playing' in session:
        time.sleep(60)
        #Generate a random category
        categories = ["Famous historical figure", "Capital city of a country", "Popular movie title", "Famous landmark", "Type of cuisine", "Sports team", "Popular Sitcom Character", "Musical instrument", "Types of flower", "Poupular Movie character"]
        category = random.choice(categories)
        
        #Generate a word for the category using OpenAI
        openai.api_key=api_key
        prompt = f"Suggest a {category}. Only show the word, not the definition. Remove the dot at the end."
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        word = response.choices[0].message.content
        word = word.lower()
        word = word.replace(".", "")

        #Generate 10 clues for the word using OpenAI
        prompt = f"Suggest 10 short sentences that will serve as clues for someone to guess the {category},{word}. Don't include the word in the clues."
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        clue = response.choices[0].message.content
        clue_list = clue.splitlines()

        #return game_data
        session['game_category'], session['game_clues'], session['game_answer'] = category, clue_list, word
        session['sequence'] = 0
        session['generated'] = "True"
        return redirect(url_for('views.play_game'))
    else:
        return redirect(url_for('views.home'))
    
@views.route('/')
def home():
    session['playing'] = "True"
    return render_template("index.html")

#play the game
@views.route('/play', methods=['GET', 'POST'])
def play_game():
    if 'playing' in session and 'generated' in session:
        game_category, game_clues, game_answer = session.get('game_category'), session.get('game_clues'), session.get('game_answer')
        if request.method == 'POST':
            if session['sequence'] > 9:
                answer=request.form['answer']
                if answer!=None and answer!="":
                    if answer.lower().strip() == game_answer.lower().strip():
                        return render_template("pass.html",category=game_category)
                    else:
                        return render_template("fail.html", category=game_category,word=game_answer.upper())
                else:
                    return render_template("play_game.html", answer=answer, rnd=session['sequence']+1, category=game_category, clue=game_clues[session['sequence']], word=game_answer)
            elif session['sequence'] <=9:
                answer=request.form['answer']
                if answer!=None and answer!="":
                    if answer.lower().strip() == game_answer.lower().strip():
                        return render_template("pass.html",category=game_category)
                    else:
                        #
                        session['sequence'] = session['sequence'] +1
                        i = session['sequence']
                        a = session['sequence'] + 1 
                        if a != 11:
                            return render_template("play_game.html", answer=answer, rnd=a, category=game_category, clue=game_clues[i], word=game_answer)
                        else:
                            return render_template("fail.html", category=game_category,word=game_answer.upper())
                else:
                    return render_template("play_game.html", answer=answer, rnd=session['sequence']+1, category=game_category, clue=game_clues[session['sequence']], word=game_answer)
            else:
                return render_template("fail.html", category=game_category,word=game_answer.upper())
        elif request.method == 'GET' and session['sequence'] <=9:
            return render_template("guess.html",rnd=1,category=game_category, clue=game_clues[0], word=game_answer)
        else:
            return render_template("fail.html", category=game_category,word=game_answer.upper())
    else:
        return redirect(url_for('views.home'))

def delete_sessions():
    for key in list(session.keys()):
        del session[key]

@views.route('/end-game')    
def exit_game():
    delete_sessions()
    return render_template('end.html')
    