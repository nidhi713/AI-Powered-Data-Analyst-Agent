from graph import graph

state = {
    "csv_file": "data.csv",
    "question": "Which department has highest average salary?"
}

result = graph.invoke(state)

print("\nFINAL ANSWER:\n")
print(result["answer"])