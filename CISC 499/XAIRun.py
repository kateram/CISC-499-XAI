import OpenAIconnector
import PostgresConnector
import read_files

if __name__ == "__main__":
    # connect to openai and database
    #api_key = #ADD API KEY HERE
    connector = OpenAIconnector.OpenAIConnector(api_key=api_key, model="gpt-4o", temperature=0.0)
    #db = PostgresConnector.PostgresDB(ADD DB CONNECTION CREDENTIALS HERE)
    db.connect()


    # Read each file containing the initial program 
    folder_name = "499programs-main"  
    python_files = read_files.read_python_files(folder_name)

    
    for file_name, program in python_files.items():
        # Get GPT to explain the given code
        explanation = connector.explain_code(program)

        # Get GPT to generate code using the given explanation
        generated_code = connector.generate_code(explanation)

        # Store results in the database
        query = """
                INSERT INTO runresults (initial_program, explanation,generated_program, filename )
                VALUES (%s, %s, %s, %s)
                """
        
        data = (program,explanation,generated_code,file_name)
        db.execute_query(query,data)
        print(file_name, "is done")

    db.close()
    print("Done!")
    

