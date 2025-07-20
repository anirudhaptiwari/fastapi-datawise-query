import fastapi
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# The dictionary of pre-calculated answers
ANSWERS = {
    "What is the total sales of Keyboard in Fisherport?": 6016,
    "How many sales reps are there in New York?": 43,
    "What is the average sales for Mouse in Wisconsin?": 545.0,
    "On what date did Kurt Rice Sr. make the highest sale in Harmonfield?": "No sales found for this rep in this city.",
    "What is the total sales of Pants in Port Gladycebury?": 7597,
    "How many sales reps are there in Delaware?": 40,
    "What is the average sales for Pants in Oregon?": 528.4545454545455,
    "On what date did Gerald Lowe make the highest sale in Port Abby?": "No sales found for this rep in this city.",
    "What is the total sales of Shoes in Carson?": 8387,
    "How many sales reps are there in Florida?": 40,
    "What is the average sales for Mouse in Pennsylvania?": 508.25,
    "On what date did Marian Ward make the highest sale in Port Lon?": "No sales found for this rep in this city.",
    "What is the total sales of Chair in Berkeley?": 1510,
    "How many sales reps are there in Colorado?": 45,
    "What is the average sales for Chair in Arkansas?": 260.75,
    "On what date did Judith Mueller make the highest sale in Harmonfield?": "No sales found for this rep in this city.",
    "What is the total sales of Car in Stehrboro?": 1552,
    "How many sales reps are there in Mississippi?": 44,
    "What is the average sales for Pants in Georgia?": 615.5833333333334,
    "On what date did Marguerite Harvey-Wiegand make the highest sale in Lake Kalihaven?": "No sales found for this rep in this city."
}

# Your email for the header
USER_EMAIL = "21f3001420@ds.study.iitm.ac.in"

app = fastapi.FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/query")
async def handle_query(q: str):
    """
    Handles a GET request to /query?q=...
    Looks up the pre-calculated answer and returns it.
    """
    # Look up the answer in our dictionary
    answer = ANSWERS.get(q, "Question not found in the pre-calculated list.")
    
    # Create the JSON response with the custom X-Email header
    response = JSONResponse(content={"answer": answer})
    response.headers["X-Email"] = USER_EMAIL
    
    return response

# Default route for checking if the server is running
@app.get("/")
def read_root():
    return {"message": "API is running. Use the /query endpoint to ask questions."}
