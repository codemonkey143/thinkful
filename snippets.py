import argparse
import logging
import psycopg2


# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgresSQL")
connection = psycopg2.connect(database="snippets")
logging.debug("connected to PostgresSQL")


def put(name, snippet):
    logging.info("Storing snippet {!r}{!r}".format(name,snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command,(name,snippet))
    connection.commit()
    logging.debug("snippet stored successfully.")
    return name,snippet
    
def get(name):
    logging.info("getting snippet {!r}".format(name))
    cursor = connection.cursor()
    cursor.execute("select message from snippets where keyword=%s",(name,))
    row = cursor.fetchone()
    connection.commit()
    logging.debug("snippet fetched successfully.")
    return row[0]
    
def main():
    logging.info("hello")
    parser = argparse.ArgumentParser(description = 'store retreive snippet of text')
    subparser = parser.add_subparsers(dest="command",help='Available commands')
    
    #subparser for the put command:
    #usage python3 .py --type put --name list --snippet "A sequence of things - created using[]"
    #python3 snippets.py put list "A sequence of thing - created using []"
    
    logging.debug("constructing subparser put command")
    put_parser = subparser.add_parser("put",help="Store a snippet")
    put_parser.add_argument("name",help="name of the snippet")
    put_parser.add_argument("snippet",help="Snippet text")
    
    logging.debug("constructing subparser get command")
    get_parser = subparser.add_parser("get",help="getting a snippet")
    get_parser.add_argument("name",help="name of the snippet")
    
    arguments = parser.parse_args()
    
    # Convert parsed arguments from Namespace to dictonary
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name,snippet = put(**arguments)
        print ("Store {!r} ad {!r}".format(snippet,name))
    elif command == "get":
        snippet = get(**arguments)
        print ("retreived snippet: {!r}".format(snippet))
    
if __name__ == '__main__':
    main()
    