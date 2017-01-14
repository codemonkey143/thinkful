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
    #cursor = connection.cursor()
    with connection,connection.cursor() as cursor:
        try:
            command = "insert into snippets values (%s, %s)"
            cursor.execute(command,(name,snippet))
        except psycopg2.IntegrityError as e:
            connection.rollback()
            command = "update snippets set message=%s where keyword=%s"
    
    logging.debug("snippet stored successfully.")
    return name,snippet
    
def get(name):
    logging.info("getting snippet {!r}".format(name))
    with connection,connection.cursor() as cursor:
        if name:
            cursor.execute("select message from snippets where keyword=%s",(name,))
            row = cursor.fetchone()
        else:
            cursor.execute("select message from snippet where keyword=%s",(list,))
    
    logging.debug("snippet fetched successfully.")
    if not row:
        return "404: Snippet Not Found"
    return row[0]
    
def no_arg():
    logging.info("getting default snippet ".format())
    with connection,connection.cursor() as cursor:
        cursor.execute("select * from snippets order by keyword")
        #cursor.execute("select message from snippets where keyword=%s",('delete',))
        row = cursor.fetchone()
    logging.debug("default snippet fecthed successfully")
    return row
    
    
def search(name):
    logging.info("searching snippet")
    with connection,connection.cursor() as cursor:
        cursor.execute("select * from snippets where keyword LIKE '%delete%'")
        row = cursor.fetchall()
    logging.debug("fecthed successfully")
    return row
    
def main():
    logging.info("hello")
    parser = argparse.ArgumentParser(description = 'store retreive snippet of text')
    subparser = parser.add_subparsers(dest="command",help='Available commands')
    
    #subparser for the put command:
    #usage python3 .py --type put --name list --snippet "A sequence of things - created using[]"
    #python3 snippets.py put list "A sequence of thing - created using []"
    
    #put method
    logging.debug("constructing subparser put command")
    put_parser = subparser.add_parser("put",help="Store a snippet")
    put_parser.add_argument("name",help="name of the snippet")
    put_parser.add_argument("snippet",help="Snippet text")
    
    #get method
    logging.debug("constructing subparser get command")
    get_parser = subparser.add_parser("get",help="getting a snippet")
    get_parser.add_argument("name",help="name of the snippet")
    
    #no_arg method
    logging.debug("constructing subparser for no arguments")
    no_parser = subparser.add_parser("no_arg",help="just put none")
    
    #search method:
    logging.debug("constructing subparser for search argument")
    search_parser = subparser.add_parser("search",help="search with snippet")
    search_parser.add_argument("name",help="search element")
    

    #parsing the arguments
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
    elif command == "no_arg":
        print ("retrived snippet")
        snippet = no_arg(**arguments)
        for item in snippet:
            print ("{!r}".format(item))
    elif command == "search":
        snippet = search(**arguments)
        print("your result:{!r}".format(snippet))
    
if __name__ == '__main__':
    main()