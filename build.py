#!/usr/bin/python3
import csscompressor
import time

style_name = """
  _   __  ___  ___  ___ _____ 
 | | / / / _ \ |  \/  ||_   _|
 | |/ / / /_\ \| .  . |  | | 
 |    \ |  _  || |\/| |  | |  
 | |\  \| | | || |  | | _| |_ 
 \_| \_/\_| |_/\_|  |_/ \___/                          
"""

subreddit_name = "Kami"

authors = [
    "Haruka-sama", # Original theme creator
    #"", # Add additional authors here
]

source_css = [
    "header.css", # Header
    "sidebar.css", # Sidebar
    #"", # Add additional sources here
]


def gen_sub_info():
    subreddit_info = {}

    # Get the subreddit name
    subreddit_info["subreddit"] = subreddit_name

    # Get the stylesheet authors
    if len(authors) == 0:
        subreddit_info["authors"] = "/u/Haruka-sama"
    elif len(authors) == 1:
        subreddit_info["authors"] = "/u/" + authors[0]
    else:
        subreddit_info["authors"] = ""
        for author in authors[:-1]:
            subreddit_info["authors"] += "/u/{}, ".format(author)
        else:
            subreddit_info["authors"] += "/u/{}.".format(authors[-1])
        subreddit_info["authors"] = subreddit_info["authors"][::-1].replace(",","& ",1)[::-1]

    with open("build.no", 'r') as build_number:
        subreddit_info["build"] =  build_number.read()
    
    with open("build.no", 'w') as build_number:
        build_number.write(str(int(subreddit_info["build"]) + 1))
    

    return subreddit_info

# File Generation Functions
def comment_header(subreddit_info):
    css_comment = """/*
    KAMI CSS theme by /u/Haruka-sama for /r/{subreddit}; build #{build}
    Authors: {authors}
*/
""".format(**subreddit_info)
    return css_comment

if __name__ == "__main__":
    start_time = time.time()
    css_output = ""
    subreddit_info = gen_sub_info()

    print(style_name)
    print("generating stylesheet for /r/{subreddit}, build #{build}\n".format(**subreddit_info))

    # Add aditional css files
    for file in source_css:
        print("\tadding: {}".format(file))
        try:
            css_output += open("src/" + file, 'r').read()
        except Exception as e:
            print("\tError adding {}".format(file))
            
        
    # Write css to file
    with open("output.css", 'w') as output:
          output.write(comment_header(subreddit_info) + css_output)  
    with open("output_minifided.css", 'w') as output:
        output.write(comment_header(subreddit_info) + csscompressor.compress(css_output))
    
    end_time = time.time()
    print("\nSuccesfully generated css file!")
    print("\tTook {} seconds!".format(str(end_time - start_time)))