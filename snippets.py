import logging
import argparse

logging.basicConfig(filename="snippets.log",level=logging.DEBUG)

def put(name,snippet):
    """
    Store a snippet with an associated name.
    
    Returns the name and snippet
    """
    logging.error("FIXME: Unimplemented - put({!r},{!r})".format(name,snippet))
    return name,snippet

def get(name):
    """
    Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""

def main():
    logging.info("Constructing a parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippet of text")
    subparser = parser.add_subparsers(dest="command",help="Available commands")
    
    #subparse for the put command
    logging.debug("constructing put subparser")
    put_parser = subparser.add_parser("put",help="store a snippet")
    put_parser.add_argument("name",help="Name of the snippet")
    put_parser.add_argument("snippet",help="snippet text")
    arguments = parser.parse_args()
    
    #convert parsed arguments from NameSpace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
    if command == "put":
        name,snippet = put(**arguments)
        print ("Stored {!r} as {!r}".format(snippet,name))
    elif command == "get":
        snippet = get(**arguments)
        print ("Retrived snippet: {!r}".format(snippet))
    
if __name__ == "__main__":
    main()
