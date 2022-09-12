import time
import random
import sys
import enchant

#listLibrary: Contains Words List
def listLibrary():
    list_library=['ABOUT', 'ALERT', 'ARGUE', 'BEACH', 'ABOVE', 'ALIKE', 'ARISE', 'BEGAN', 'ABUSE', 'ALIVE', 'ARRAY', 'BEGIN', 'ACTOR', 'ALLOW', 'ASIDE', 'BEGUN', 'ACUTE', 'ALONE', 'ASSET', 'BEING', 'ADMIT', 'ALONG', 'AUDIO', 'BELOW', 'ADOPT', 'ALTER', 'AUDIT', 'BENCH', 'ADULT', 'AMONG', 'AVOID', 'BILLY', 'AFTER', 'ANGER', 'AWARD', 'BIRTH', 'AGAIN', 'ANGLE', 'AWARE', 'BLACK', 'AGENT', 'ANGRY', 'BADLY', 'BLAME', 'AGREE', 'APART', 'BAKER', 'BLIND', 'AHEAD', 'APPLE', 'BASES', 'BLOCK', 'ALARM', 'APPLY', 'BASIC', 'BLOOD', 'ALBUM', 'ARENA', 'BASIS', 'BOARD', 'BOOST', 'BUYER', 'CHINA', 'COVER', 'BOOTH', 'CABLE', 'CHOSE', 'CRAFT', 'BOUND', 'CALIF', 'CIVIL', 'CRASH', 'BRAIN', 'CARRY', 'CLAIM', 'CREAM', 'BRAND', 'CATCH', 'CLASS', 'CRIME', 'BREAD', 'CAUSE', 'CLEAN', 'CROSS', 'BREAK', 'CHAI', 'CLEAR', 'CROWD', 'BREED', 'CHAIR', 'CLICK', 'CROWN', 'BRIEF', 'CHART', 'CLOCK', 'CURVE', 'BRING', 'CHASE', 'CLOSE', 'CYCLE', 'BROAD', 'CHEAP', 'COACH', 'DAILY', 'BROKE', 'CHECK', 'COAST', 'DANCE', 'BROWN', 'CHEST', 'COULD', 'DATED', 'BUILD', 'CHIEF', 'COUNT', 'DEALT', 'BUILT', 'CHILD', 'COURT', 'DEATH', 'DEBUT', 'ENTRY', 'FORTH', 'GROUP', 'DELAY', 'EQUAL', 'FORTY', 'GROWN', 'DEPTH', 'ERROR', 'TOTAL', 'SHOOT', 'SPOKE', 'TAKEN', 'TOUCH', 'SHORT', 'SPORT', 'TASTE', 'TOUGH', 'SHOWN', 'STAFF', 'TAXES', 'TOWER', 'SIGHT', 'STAGE', 'TEACH', 'TRACK', 'SINCE', 'STAKE', 'TEETH', 'TRADE', 'SIXTH', 'STAND', 'TERRY', 'TRAIN', 'SIXTY', 'START', 'TEXAS', 'TREAT', 'SIZED', 'STATE', 'THANK', 'TREND', 'SKILL', 'STEAM', 'THEFT', 'TRIAL', 'SLEEP', 'STEEL', 'THEIR', 'TRIED', 'SLIDE', 'STICK', 'THEME', 'TRIES', 'SMALL', 'STILL', 'THERE', 'TRUCK', 'SMART', 'STOCK', 'THESE', 'TRULY', 'SMILE', 'STONE', 'THICK', 'TRUST', 'SMITH', 'STOOD', 'THING', 'TRUTH', 'SMOKE', 'STORE', 'THINK', 'TWICE', 'SOLID', 'STORM', 'THIRD', 'UNDER', 'SOLVE', 'STORY', 'THOSE', 'UNDUE', 'SORRY', 'STRIP', 'THREE', 'UNION', 'SOUND', 'STUCK', 'THREW', 'UNITY', 'SOUTH', 'STUDY', 'THROW', 'UNTIL', 'SPACE', 'STUFF', 'TIGHT', 'UPPER', 'UPSET', 'WHOLE', 'WASTE', 'WOUND', 'URBAN', 'WHOSE', 'WATCH', 'WRITE', 'USAGE', 'WOMAN', 'WATER', 'WRONG', 'USUAL', 'WOMEN', 'WHEEL', 'WROTE', 'VALID', 'WORLD', 'WHERE', 'YIELD', 'VALUE', 'WORRY', 'WHICH', 'YOUNG', 'VIDEO', 'WORSE', 'WHILE', 'YOUTH', 'VIRUS', 'WORST', 'WHITE', 'WORTH', 'VISIT', 'WOULD', 'VITAL', 'VOICE']
    return list_library

# playerDetail: Store player detail
def playerDetail():
    player_name=input("Enter Your Name:   ")
    return player_name

#greetingsOfDay: Greet player according to system time
def greetingsOfDay():
         struct_type=time.localtime()
         hour=int(time.strftime("%H",struct_type))
         if hour>=0 and hour<12:
             return "Good Morning"
         elif hour>=12 and hour<17:
             return "Good Afternoon"
         elif hour>=17 and hour<20:
             return "Good Evening"
         else:
             return "Good Night"

#introduction_to_game: Introduce Rules of the game to player
def introductionToGame():
    input("{}, {}. Welcome To The World Puzzle Game: ".format(greetingsOfDay(),playerDetail())+"[Press Any Key To Continue Game]  ")
    print("\nLet's take a look at the rules to play this Game: ")
    print("\n1.  You have given a word containing 5 Letters.")
    print("2.  You have total 5 chance, One chance for each word to arrange these letters and form a meaningful Word.")
    print("3.  For each Correct word you get +1 Score and for each Incorrect word you loose -1 Score.")
    print("4.  You could score maximum 5 Points and if you don\'t get maximum score then you have Chance to play again.\n")
    game_began_choice=input("So Let\'s began with the Game [Y/N]:   ")
    print()
    return game_began_choice

#choiceToPlay: After showing Rules, Provide user a choice to play or exit
def choiceToPlay(game_began_choice):
    if game_began_choice=="Y":
        print()
        return gameLogic()
    elif game_began_choice=="N":
        Quit_game_choice=input("Do you want to Quit Game[Y/N]:  ")
        if Quit_game_choice=="Y":
            print("\n-------Game Ended-------")
            sys.exit()
        else:
           print("\n")
           return gameLogic()
#wordCheaker : Check Meaningfulness of Word from dictionary
def wordCheaker(word,original_word):
       original_word_element_list=list(original_word)
       original_word_element_list.sort()
       word_element_list=list(word)
       word_element_list.sort()
       if original_word_element_list==word_element_list:
            dictionary_english=enchant.Dict("en_US")
            return dictionary_english.check(word)
       else:
           return False

#gameLogic: Actual Logic how game works
def gameLogic():
    words_original_list = random.sample(listLibrary(), 5)
    words_shuffle_list = []
    for s in words_original_list:
        words_shuffle_list.append(''.join(random.sample(s, len(s))))
    i, score = 0, 0
    for s in words_shuffle_list:
        print("Arrange the Letter to form a valid Word: ", s)
        input_word=input("Enter Word: ").upper()
        if words_original_list[i] == input_word or wordCheaker(input_word,words_original_list[i]):
            print("Result: Correct")
            score += 1
        else:
            print("Correct Answer:  ",words_original_list[i])
            print("Result: Incorrect")
            score -= 1
        i += 1
        print()
    return score
#postGameGreet: Great user according to Score
def postGameGreet(score):
    if score==5:
        post_game_greeting="Hurrah !"
    elif score>=1 and score<=4:
        post_game_greeting="Good"
    elif score >= -5 and score <= 0:
        post_game_greeting = "Low Score!"
    else:
        post_game_greeting=""
    return post_game_greeting

# dashHiglighter : To highlight Score
def dashHighlighter():
    for _ in range(39):
        print("-",end="")
    print()

# try_again: If User do not get Maximum marks and user want to play again
def try_again(score):
    if score>= -5 and score<5:
        try_again_choice=input("\nDo you want to play again[Y/N]: ")
        if try_again_choice=="Y":
            print("\n")
            showScore(gameLogic())
        else:
            print("\n---------Game Ended---------")
            sys.exit()
#showScore: Process and Show Score
def showScore(score):
    dashHighlighter()
    print("{},Your Net Score is : {} Points".format(postGameGreet(score),score))
    dashHighlighter()
    try_again(score)


showScore(choiceToPlay(introductionToGame()))


