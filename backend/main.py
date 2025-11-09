from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from openai import OpenAI
import os
from dotenv import load_dotenv
import json

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust for frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment variables
load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Product database
PRODUCT_DATABASE = [
    {"id": 1, "name": "Coles Cream Cheese 250g", "price": 9.68, "stock": 0, "aisle": "1A", "popularity": 76, "quality": "standard"},
    {"id": 2, "name": "Coles Full Cream Milk 1L", "price": 19.53, "stock": 34, "aisle": "5B", "popularity": 62, "quality": "premium"},
    {"id": 3, "name": "Cream Cheese 250g", "price": 6.43, "stock": 0, "aisle": "4A", "popularity": 61, "quality": "budget"},
    {"id": 4, "name": "Budget Cream Cheese 250g", "price": 14.35, "stock": 0, "aisle": "2B", "popularity": 91, "quality": "standard"},
    {"id": 5, "name": "Organic Choice Coles Butter 500g", "price": 14.76, "stock": 0, "aisle": "2E", "popularity": 80, "quality": "premium"},
    {"id": 6, "name": "FreshFarm Cream Cheese 250g", "price": 9.93, "stock": 191, "aisle": "3D", "popularity": 73, "quality": "standard"},
    {"id": 7, "name": "Budget Cheddar Cheese 500g", "price": 19.06, "stock": 0, "aisle": "4B", "popularity": 72, "quality": "standard"},
    {"id": 8, "name": "Organic Choice Fresh Milk 2L", "price": 5.34, "stock": 0, "aisle": "1A", "popularity": 77, "quality": "standard"},
    {"id": 9, "name": "Coles Cream Cheese 250g", "price": 2.92, "stock": 0, "aisle": "3D", "popularity": 91, "quality": "premium"},
    {"id": 10, "name": "Homebrand Coles Butter 500g", "price": 11.64, "stock": 0, "aisle": "3B", "popularity": 62, "quality": "budget"},
    {"id": 11, "name": "Budget Fresh Milk 2L", "price": 13.09, "stock": 143, "aisle": "5A", "popularity": 77, "quality": "budget"},
    {"id": 12, "name": "FreshFarm Greek Yogurt 1kg", "price": 7.42, "stock": 0, "aisle": "1A", "popularity": 72, "quality": "budget"},
    {"id": 13, "name": "Homebrand Greek Yogurt 1kg", "price": 2.44, "stock": 0, "aisle": "4D", "popularity": 70, "quality": "budget"},
    {"id": 14, "name": "FreshFarm Organic Milk 2L", "price": 13.9, "stock": 184, "aisle": "2D", "popularity": 73, "quality": "standard"},
    {"id": 15, "name": "Budget Cream Cheese 250g", "price": 23.47, "stock": 0, "aisle": "3D", "popularity": 94, "quality": "premium"},
    {"id": 16, "name": "Coles Cream Cheese 250g", "price": 16.92, "stock": 86, "aisle": "2B", "popularity": 83, "quality": "standard"},
    {"id": 17, "name": "Fresh Milk 2L", "price": 20.68, "stock": 0, "aisle": "3E", "popularity": 85, "quality": "standard"},
    {"id": 18, "name": "Budget Organic Milk 2L", "price": 24.67, "stock": 0, "aisle": "1D", "popularity": 62, "quality": "premium"},
    {"id": 19, "name": "Budget Coles Butter 500g", "price": 22.44, "stock": 0, "aisle": "2A", "popularity": 77, "quality": "budget"},
    {"id": 20, "name": "Budget Fresh Milk 2L", "price": 11.01, "stock": 38, "aisle": "4E", "popularity": 95, "quality": "premium"},
    {"id": 21, "name": "Wholemeal Bread", "price": 9.75, "stock": 0, "aisle": "5D", "popularity": 67, "quality": "budget"},
    {"id": 22, "name": "Bagels 6pk", "price": 24.38, "stock": 0, "aisle": "4D", "popularity": 69, "quality": "budget"},
    {"id": 23, "name": "Coles Multigrain Bread", "price": 5.14, "stock": 0, "aisle": "4A", "popularity": 82, "quality": "standard"},
    {"id": 24, "name": "FreshFarm Muffins 6pk", "price": 23.11, "stock": 0, "aisle": "2C", "popularity": 73, "quality": "standard"},
    {"id": 25, "name": "Coles Croissants 4pk", "price": 15.95, "stock": 59, "aisle": "5B", "popularity": 95, "quality": "budget"},
    {"id": 26, "name": "White Sandwich Bread", "price": 23.67, "stock": 115, "aisle": "3B", "popularity": 82, "quality": "standard"},
    {"id": 27, "name": "Organic Choice Wholemeal Bread", "price": 18.3, "stock": 0, "aisle": "3D", "popularity": 62, "quality": "premium"},
    {"id": 28, "name": "Organic Choice Coles Multigrain Bread", "price": 5.6, "stock": 0, "aisle": "3B", "popularity": 64, "quality": "budget"},
    {"id": 29, "name": "Homebrand Muffins 6pk", "price": 3.31, "stock": 0, "aisle": "5C", "popularity": 69, "quality": "premium"},
    {"id": 30, "name": "Organic Choice Bagels 6pk", "price": 18.91, "stock": 0, "aisle": "3E", "popularity": 89, "quality": "standard"},
    {"id": 31, "name": "Organic Choice Coles Multigrain Bread", "price": 20.84, "stock": 0, "aisle": "2E", "popularity": 72, "quality": "budget"},
    {"id": 32, "name": "Budget Bagels 6pk", "price": 18.4, "stock": 63, "aisle": "1C", "popularity": 88, "quality": "standard"},
    {"id": 33, "name": "Organic Choice Artisan Sourdough Loaf", "price": 2.2, "stock": 102, "aisle": "2E", "popularity": 73, "quality": "standard"},
    {"id": 34, "name": "Organic Choice Bagels 6pk", "price": 17.44, "stock": 79, "aisle": "1D", "popularity": 95, "quality": "premium"},
    {"id": 35, "name": "FreshFarm Croissants 4pk", "price": 8.02, "stock": 127, "aisle": "2D", "popularity": 66, "quality": "budget"},
    {"id": 36, "name": "FreshFarm Coles Multigrain Bread", "price": 5.47, "stock": 0, "aisle": "3A", "popularity": 89, "quality": "standard"},
    {"id": 37, "name": "Coles Croissants 4pk", "price": 7.47, "stock": 0, "aisle": "5E", "popularity": 70, "quality": "standard"},
    {"id": 38, "name": "FreshFarm Artisan Sourdough Loaf", "price": 16.58, "stock": 0, "aisle": "5C", "popularity": 94, "quality": "budget"},
    {"id": 39, "name": "FreshFarm Artisan Sourdough Loaf", "price": 22.41, "stock": 0, "aisle": "3C", "popularity": 72, "quality": "premium"},
    {"id": 40, "name": "FreshFarm Wholemeal Bread", "price": 7.73, "stock": 0, "aisle": "5A", "popularity": 73, "quality": "budget"},
    {"id": 41, "name": "Budget Coles Jasmine Rice 2kg", "price": 9.66, "stock": 155, "aisle": "1D", "popularity": 73, "quality": "premium"},
    {"id": 42, "name": "Homebrand Coles Jasmine Rice 2kg", "price": 5.02, "stock": 0, "aisle": "3C", "popularity": 85, "quality": "budget"},
    {"id": 43, "name": "Homebrand Coles Jasmine Rice 2kg", "price": 2.81, "stock": 165, "aisle": "3A", "popularity": 76, "quality": "premium"},
    {"id": 44, "name": "Coles Tomato Sauce 700ml", "price": 5.02, "stock": 27, "aisle": "5D", "popularity": 80, "quality": "premium"},
    {"id": 45, "name": "Coles Jasmine Rice 2kg", "price": 19.73, "stock": 117, "aisle": "5A", "popularity": 78, "quality": "standard"},
    {"id": 46, "name": "Budget Peanut Butter 500g", "price": 24.9, "stock": 0, "aisle": "3D", "popularity": 79, "quality": "budget"},
    {"id": 47, "name": "Coles Jasmine Rice 2kg", "price": 17.96, "stock": 0, "aisle": "4A", "popularity": 90, "quality": "budget"},
    {"id": 48, "name": "Homebrand Olive Oil 1L", "price": 19.2, "stock": 129, "aisle": "1B", "popularity": 68, "quality": "premium"},
    {"id": 49, "name": "Homebrand Peanut Butter 500g", "price": 12.6, "stock": 181, "aisle": "2E", "popularity": 88, "quality": "premium"},
    {"id": 50, "name": "Homebrand Long Grain Rice 5kg", "price": 5.35, "stock": 46, "aisle": "1C", "popularity": 72, "quality": "budget"},
    {"id": 51, "name": "Baked Beans 420g", "price": 9.8, "stock": 0, "aisle": "3C", "popularity": 80, "quality": "standard"},
    {"id": 52, "name": "Homebrand Coles Jasmine Rice 2kg", "price": 12.89, "stock": 115, "aisle": "2B", "popularity": 61, "quality": "budget"},
    {"id": 53, "name": "Long Grain Rice 5kg", "price": 5.45, "stock": 0, "aisle": "4D", "popularity": 73, "quality": "premium"},
    {"id": 54, "name": "Olive Oil 1L", "price": 7.44, "stock": 0, "aisle": "4A", "popularity": 68, "quality": "premium"},
    {"id": 55, "name": "Instant Ramen 5x", "price": 23.73, "stock": 33, "aisle": "3A", "popularity": 71, "quality": "standard"},
    {"id": 56, "name": "Budget Instant Ramen 5x", "price": 9.59, "stock": 181, "aisle": "5B", "popularity": 87, "quality": "premium"},
    {"id": 57, "name": "Organic Choice Long Grain Rice 5kg", "price": 21.38, "stock": 0, "aisle": "2E", "popularity": 84, "quality": "budget"},
    {"id": 58, "name": "Homebrand Coles Jasmine Rice 2kg", "price": 13.78, "stock": 0, "aisle": "2A", "popularity": 64, "quality": "premium"},
    {"id": 59, "name": "Long Grain Rice 5kg", "price": 19.99, "stock": 185, "aisle": "3D", "popularity": 92, "quality": "standard"},
    {"id": 60, "name": "Budget Peanut Butter 500g", "price": 18.81, "stock": 22, "aisle": "3C", "popularity": 81, "quality": "budget"},
    {"id": 61, "name": "FreshFarm Pork Chops 1kg", "price": 13.84, "stock": 41, "aisle": "1A", "popularity": 73, "quality": "budget"},
    {"id": 62, "name": "Budget Chicken Breast 1kg", "price": 16.06, "stock": 0, "aisle": "5D", "popularity": 88, "quality": "standard"},
    {"id": 63, "name": "Homebrand Pork Chops 1kg", "price": 23.06, "stock": 0, "aisle": "3A", "popularity": 89, "quality": "premium"},
    {"id": 64, "name": "Coles Chicken Breast 1kg", "price": 21.62, "stock": 10, "aisle": "5A", "popularity": 66, "quality": "standard"},
    {"id": 65, "name": "Whole Chicken 1.5kg", "price": 23.26, "stock": 0, "aisle": "1D", "popularity": 83, "quality": "standard"},
    {"id": 66, "name": "Coles Whole Chicken 1.5kg", "price": 12.63, "stock": 128, "aisle": "3B", "popularity": 81, "quality": "standard"},
    {"id": 67, "name": "FreshFarm Bacon 250g", "price": 18.1, "stock": 37, "aisle": "5A", "popularity": 88, "quality": "standard"},
    {"id": 68, "name": "FreshFarm Lamb Cutlets 800g", "price": 10.95, "stock": 128, "aisle": "1A", "popularity": 71, "quality": "premium"},
    {"id": 69, "name": "Budget Pork Chops 1kg", "price": 14.04, "stock": 187, "aisle": "4C", "popularity": 95, "quality": "budget"},
    {"id": 70, "name": "Organic Choice Lamb Cutlets 800g", "price": 7.33, "stock": 0, "aisle": "3A", "popularity": 66, "quality": "budget"},
    {"id": 71, "name": "Lamb Cutlets 800g", "price": 8.8, "stock": 164, "aisle": "3A", "popularity": 85, "quality": "budget"},
    {"id": 72, "name": "Organic Choice Sausages 500g", "price": 14.44, "stock": 0, "aisle": "1E", "popularity": 83, "quality": "standard"},
    {"id": 73, "name": "Bacon 250g", "price": 16.29, "stock": 0, "aisle": "3A", "popularity": 94, "quality": "budget"},
    {"id": 74, "name": "Whole Chicken 1.5kg", "price": 19.93, "stock": 160, "aisle": "3C", "popularity": 78, "quality": "premium"},
    {"id": 75, "name": "Coles Pork Chops 1kg", "price": 14.31, "stock": 186, "aisle": "1D", "popularity": 80, "quality": "premium"},
    {"id": 76, "name": "FreshFarm Whole Chicken 1.5kg", "price": 24.4, "stock": 184, "aisle": "2C", "popularity": 62, "quality": "budget"},
    {"id": 77, "name": "Homebrand Bacon 250g", "price": 18.26, "stock": 155, "aisle": "2E", "popularity": 85, "quality": "budget"},
    {"id": 78, "name": "FreshFarm Sausages 500g", "price": 15.0, "stock": 150, "aisle": "3E", "popularity": 81, "quality": "budget"},
    {"id": 79, "name": "Homebrand Pork Chops 1kg", "price": 24.35, "stock": 156, "aisle": "2A", "popularity": 89, "quality": "budget"},
    {"id": 80, "name": "Coles Sausages 500g", "price": 3.36, "stock": 0, "aisle": "1A", "popularity": 80, "quality": "standard"},
    {"id": 81, "name": "Potatoes 2kg", "price": 17.26, "stock": 115, "aisle": "3D", "popularity": 79, "quality": "premium"},
    {"id": 82, "name": "Homebrand Pink Lady Apples 1kg", "price": 9.3, "stock": 0, "aisle": "3D", "popularity": 81, "quality": "premium"},
    {"id": 83, "name": "Homebrand Lettuce 1 head", "price": 14.14, "stock": 0, "aisle": "2E", "popularity": 71, "quality": "standard"},
    {"id": 84, "name": "Coles Bananas 1kg", "price": 6.84, "stock": 176, "aisle": "1A", "popularity": 73, "quality": "premium"},
    {"id": 85, "name": "Budget Granny Smith Apples 1kg", "price": 15.37, "stock": 151, "aisle": "1D", "popularity": 65, "quality": "budget"},
    {"id": 86, "name": "Granny Smith Apples 1kg", "price": 4.39, "stock": 0, "aisle": "2D", "popularity": 81, "quality": "premium"},
    {"id": 87, "name": "Budget Granny Smith Apples 1kg", "price": 5.91, "stock": 19, "aisle": "1D", "popularity": 88, "quality": "standard"},
    {"id": 88, "name": "Coles Tomatoes 500g", "price": 11.36, "stock": 0, "aisle": "2B", "popularity": 79, "quality": "premium"},
    {"id": 89, "name": "Coles Coles Carrots 1kg", "price": 23.44, "stock": 0, "aisle": "1E", "popularity": 71, "quality": "budget"},
    {"id": 90, "name": "Tomatoes 500g", "price": 22.26, "stock": 0, "aisle": "1C", "popularity": 77, "quality": "standard"},
    {"id": 91, "name": "Coles Tomatoes 500g", "price": 8.61, "stock": 0, "aisle": "2D", "popularity": 74, "quality": "budget"},
    {"id": 92, "name": "Coles Potatoes 2kg", "price": 5.55, "stock": 0, "aisle": "3A", "popularity": 72, "quality": "standard"},
    {"id": 93, "name": "Coles Coles Carrots 1kg", "price": 23.97, "stock": 0, "aisle": "2E", "popularity": 92, "quality": "budget"},
    {"id": 94, "name": "Budget Bananas 1kg", "price": 19.01, "stock": 141, "aisle": "2C", "popularity": 64, "quality": "premium"},
    {"id": 95, "name": "Homebrand Pink Lady Apples 1kg", "price": 5.72, "stock": 45, "aisle": "5C", "popularity": 63, "quality": "premium"},
    {"id": 96, "name": "Coles Granny Smith Apples 1kg", "price": 23.77, "stock": 198, "aisle": "3D", "popularity": 86, "quality": "standard"},
    {"id": 97, "name": "Homebrand Pink Lady Apples 1kg", "price": 5.09, "stock": 84, "aisle": "4C", "popularity": 88, "quality": "budget"},
    {"id": 98, "name": "Budget Pink Lady Apples 1kg", "price": 22.97, "stock": 43, "aisle": "1A", "popularity": 76, "quality": "premium"},
    {"id": 99, "name": "Organic Choice Tomatoes 500g", "price": 4.56, "stock": 199, "aisle": "3B", "popularity": 88, "quality": "budget"},
    {"id": 100, "name": "Coles Carrots 1kg", "price": 6.51, "stock": 0, "aisle": "2B", "popularity": 83, "quality": "budget"},
    {"id": 101, "name": "Organic Choice Coca Cola 1.25L", "price": 16.01, "stock": 0, "aisle": "5C", "popularity": 87, "quality": "premium"},
    {"id": 102, "name": "Budget Coles Spring Water 1.5L", "price": 19.39, "stock": 64, "aisle": "4C", "popularity": 86, "quality": "premium"},
    {"id": 103, "name": "Organic Choice Coca Cola 1.25L", "price": 22.48, "stock": 155, "aisle": "1E", "popularity": 86, "quality": "premium"},
    {"id": 104, "name": "Homebrand Coffee Beans 1kg", "price": 11.11, "stock": 22, "aisle": "4D", "popularity": 78, "quality": "standard"},
    {"id": 105, "name": "Organic Choice Energy Drink 500ml", "price": 21.59, "stock": 89, "aisle": "3C", "popularity": 92, "quality": "premium"},
    {"id": 106, "name": "Coles Coffee Beans 1kg", "price": 16.5, "stock": 47, "aisle": "3D", "popularity": 60, "quality": "budget"},
    {"id": 107, "name": "Organic Choice Coles Spring Water 1.5L", "price": 19.69, "stock": 86, "aisle": "1A", "popularity": 87, "quality": "budget"},
    {"id": 108, "name": "Homebrand Energy Drink 500ml", "price": 19.71, "stock": 90, "aisle": "1C", "popularity": 70, "quality": "premium"},
    {"id": 109, "name": "FreshFarm Energy Drink 500ml", "price": 8.77, "stock": 95, "aisle": "3E", "popularity": 87, "quality": "premium"},
    {"id": 110, "name": "Coles Coffee Beans 1kg", "price": 8.89, "stock": 181, "aisle": "5C", "popularity": 67, "quality": "premium"},
    {"id": 111, "name": "Homebrand Green Tea 100pk", "price": 21.61, "stock": 0, "aisle": "4C", "popularity": 76, "quality": "premium"},
    {"id": 112, "name": "Coles Orange Juice 2L", "price": 16.93, "stock": 16, "aisle": "5B", "popularity": 78, "quality": "budget"},
    {"id": 113, "name": "Coles Orange Juice 2L", "price": 5.8, "stock": 56, "aisle": "1B", "popularity": 93, "quality": "budget"},
    {"id": 114, "name": "Coles Energy Drink 500ml", "price": 6.6, "stock": 57, "aisle": "2B", "popularity": 70, "quality": "budget"},
    {"id": 115, "name": "Budget Coles Spring Water 1.5L", "price": 8.49, "stock": 42, "aisle": "5E", "popularity": 66, "quality": "standard"},
    {"id": 116, "name": "Coles Spring Water 1.5L", "price": 14.01, "stock": 170, "aisle": "5A", "popularity": 64, "quality": "standard"},
    {"id": 117, "name": "Energy Drink 500ml", "price": 24.58, "stock": 168, "aisle": "5D", "popularity": 84, "quality": "budget"},
    {"id": 118, "name": "Organic Choice Coffee Beans 1kg", "price": 17.55, "stock": 0, "aisle": "4E", "popularity": 81, "quality": "premium"},
    {"id": 119, "name": "Budget Coca Cola 1.25L", "price": 8.32, "stock": 0, "aisle": "1E", "popularity": 77, "quality": "premium"},
    {"id": 120, "name": "Green Tea 100pk", "price": 5.77, "stock": 24, "aisle": "2C", "popularity": 68, "quality": "premium"},
    {"id": 121, "name": "Budget Trail Mix 300g", "price": 15.27, "stock": 0, "aisle": "5B", "popularity": 71, "quality": "budget"},
    {"id": 122, "name": "Organic Choice Popcorn 100g", "price": 10.5, "stock": 0, "aisle": "3E", "popularity": 83, "quality": "standard"},
    {"id": 123, "name": "Organic Choice Biscuits 250g", "price": 7.08, "stock": 124, "aisle": "5E", "popularity": 75, "quality": "budget"},
    {"id": 124, "name": "Coles Pretzels 200g", "price": 19.36, "stock": 0, "aisle": "1C", "popularity": 90, "quality": "standard"},
    {"id": 125, "name": "Chocolate Bar 50g", "price": 15.39, "stock": 0, "aisle": "4C", "popularity": 69, "quality": "standard"},
    {"id": 126, "name": "FreshFarm Coles Salted Peanuts 500g", "price": 4.42, "stock": 164, "aisle": "2E", "popularity": 70, "quality": "premium"},
    {"id": 127, "name": "Coles Popcorn 100g", "price": 11.98, "stock": 0, "aisle": "2E", "popularity": 72, "quality": "budget"},
    {"id": 128, "name": "Coles Chocolate Bar 50g", "price": 9.29, "stock": 126, "aisle": "5E", "popularity": 92, "quality": "standard"},
    {"id": 129, "name": "Homebrand Pretzels 200g", "price": 24.76, "stock": 147, "aisle": "4D", "popularity": 73, "quality": "premium"},
    {"id": 130, "name": "Coles Salted Peanuts 500g", "price": 13.57, "stock": 146, "aisle": "3D", "popularity": 62, "quality": "premium"},
    {"id": 131, "name": "Budget Coles Salted Peanuts 500g", "price": 3.82, "stock": 0, "aisle": "1A", "popularity": 89, "quality": "budget"},
    {"id": 132, "name": "Organic Choice Popcorn 100g", "price": 12.43, "stock": 48, "aisle": "3D", "popularity": 94, "quality": "standard"},
    {"id": 133, "name": "Pretzels 200g", "price": 17.93, "stock": 0, "aisle": "3D", "popularity": 65, "quality": "premium"},
    {"id": 134, "name": "FreshFarm Potato Chips 200g", "price": 19.66, "stock": 187, "aisle": "3D", "popularity": 70, "quality": "budget"},
    {"id": 135, "name": "Coles Popcorn 100g", "price": 3.98, "stock": 128, "aisle": "2D", "popularity": 89, "quality": "budget"},
    {"id": 136, "name": "FreshFarm Trail Mix 300g", "price": 22.02, "stock": 167, "aisle": "2A", "popularity": 83, "quality": "standard"},
    {"id": 137, "name": "Budget Potato Chips 200g", "price": 23.96, "stock": 0, "aisle": "4A", "popularity": 65, "quality": "standard"},
    {"id": 138, "name": "Coles Pretzels 200g", "price": 11.27, "stock": 108, "aisle": "1E", "popularity": 94, "quality": "standard"},
    {"id": 139, "name": "Organic Choice Pretzels 200g", "price": 13.6, "stock": 0, "aisle": "2C", "popularity": 87, "quality": "premium"},
    {"id": 140, "name": "Coles Chocolate Bar 50g", "price": 3.49, "stock": 57, "aisle": "5E", "popularity": 77, "quality": "premium"},
    {"id": 141, "name": "Coles Fish Fillets 1kg", "price": 2.28, "stock": 0, "aisle": "5B", "popularity": 67, "quality": "premium"},
    {"id": 142, "name": "Coles Frozen Peas 1kg", "price": 5.3, "stock": 25, "aisle": "1E", "popularity": 73, "quality": "standard"},
    {"id": 143, "name": "FreshFarm Coles Frozen Peas 1kg", "price": 3.74, "stock": 177, "aisle": "3D", "popularity": 80, "quality": "premium"},
    {"id": 144, "name": "Budget Garlic Bread 400g", "price": 11.19, "stock": 78, "aisle": "2A", "popularity": 77, "quality": "budget"},
    {"id": 145, "name": "Homebrand Fish Fillets 1kg", "price": 22.25, "stock": 191, "aisle": "2A", "popularity": 84, "quality": "premium"},
    {"id": 146, "name": "Budget Garlic Bread 400g", "price": 9.64, "stock": 0, "aisle": "4D", "popularity": 85, "quality": "premium"},
    {"id": 147, "name": "FreshFarm Ice Cream 2L", "price": 12.43, "stock": 0, "aisle": "1B", "popularity": 69, "quality": "budget"},
    {"id": 148, "name": "Fish Fillets 1kg", "price": 24.21, "stock": 113, "aisle": "4A", "popularity": 73, "quality": "standard"},
    {"id": 149, "name": "Coles Garlic Bread 400g", "price": 10.73, "stock": 12, "aisle": "5D", "popularity": 69, "quality": "standard"},
    {"id": 150, "name": "FreshFarm Garlic Bread 400g", "price": 13.58, "stock": 176, "aisle": "3A", "popularity": 65, "quality": "budget"},
    {"id": 151, "name": "Homebrand Frozen Fries 1kg", "price": 9.88, "stock": 197, "aisle": "3B", "popularity": 95, "quality": "premium"},
    {"id": 152, "name": "FreshFarm Ice Cream 2L", "price": 17.1, "stock": 95, "aisle": "2D", "popularity": 82, "quality": "premium"},
    {"id": 153, "name": "Frozen Pizza 500g", "price": 17.28, "stock": 46, "aisle": "5E", "popularity": 74, "quality": "budget"},
    {"id": 154, "name": "Organic Choice Garlic Bread 400g", "price": 8.21, "stock": 0, "aisle": "4D", "popularity": 80, "quality": "standard"},
    {"id": 155, "name": "Coles Fish Fillets 1kg", "price": 3.7, "stock": 53, "aisle": "3A", "popularity": 79, "quality": "premium"},
    {"id": 156, "name": "Coles Coles Frozen Peas 1kg", "price": 15.5, "stock": 0, "aisle": "1E", "popularity": 81, "quality": "budget"},
    {"id": 157, "name": "Coles Frozen Pizza 500g", "price": 16.67, "stock": 140, "aisle": "4C", "popularity": 69, "quality": "standard"},
    {"id": 158, "name": "Garlic Bread 400g", "price": 14.67, "stock": 0, "aisle": "3D", "popularity": 71, "quality": "premium"},
    {"id": 159, "name": "Coles Fish Fillets 1kg", "price": 20.95, "stock": 59, "aisle": "4C", "popularity": 95, "quality": "budget"},
    {"id": 160, "name": "Homebrand Frozen Pizza 500g", "price": 22.39, "stock": 0, "aisle": "1A", "popularity": 64, "quality": "budget"},
    {"id": 161, "name": "Budget Toilet Paper 12pk", "price": 4.25, "stock": 0, "aisle": "5C", "popularity": 86, "quality": "premium"},
    {"id": 162, "name": "Homebrand Toilet Paper 12pk", "price": 8.61, "stock": 0, "aisle": "2E", "popularity": 90, "quality": "budget"},
    {"id": 163, "name": "Laundry Powder 2kg", "price": 16.85, "stock": 167, "aisle": "5C", "popularity": 60, "quality": "budget"},
    {"id": 164, "name": "Organic Choice All Purpose Cleaner 750ml", "price": 7.37, "stock": 105, "aisle": "3D", "popularity": 70, "quality": "premium"},
    {"id": 165, "name": "Homebrand Air Freshener 300ml", "price": 22.53, "stock": 0, "aisle": "4B", "popularity": 70, "quality": "budget"},
    {"id": 166, "name": "Organic Choice Toilet Paper 12pk", "price": 24.84, "stock": 0, "aisle": "4E", "popularity": 91, "quality": "premium"},
    {"id": 167, "name": "Homebrand Toilet Paper 12pk", "price": 24.88, "stock": 79, "aisle": "2A", "popularity": 85, "quality": "premium"},
    {"id": 168, "name": "Air Freshener 300ml", "price": 12.91, "stock": 0, "aisle": "3B", "popularity": 94, "quality": "standard"},
    {"id": 169, "name": "Coles Air Freshener 300ml", "price": 13.46, "stock": 68, "aisle": "1D", "popularity": 74, "quality": "premium"},
    {"id": 170, "name": "Coles Air Freshener 300ml", "price": 12.41, "stock": 0, "aisle": "3E", "popularity": 77, "quality": "standard"},
    {"id": 171, "name": "Organic Choice Coles Bin Liners 50pk", "price": 12.27, "stock": 0, "aisle": "3E", "popularity": 69, "quality": "standard"},
    {"id": 172, "name": "Organic Choice Dishwashing Liquid 1L", "price": 17.33, "stock": 26, "aisle": "4B", "popularity": 89, "quality": "standard"},
    {"id": 173, "name": "Homebrand Paper Towels 6pk", "price": 19.17, "stock": 96, "aisle": "3C", "popularity": 62, "quality": "standard"},
    {"id": 174, "name": "Homebrand Coles Bin Liners 50pk", "price": 19.16, "stock": 0, "aisle": "4B", "popularity": 89, "quality": "budget"},
    {"id": 175, "name": "Homebrand Air Freshener 300ml", "price": 20.33, "stock": 0, "aisle": "2B", "popularity": 65, "quality": "budget"},
    {"id": 176, "name": "Homebrand Air Freshener 300ml", "price": 19.64, "stock": 35, "aisle": "3A", "popularity": 74, "quality": "budget"},
    {"id": 177, "name": "Budget Paper Towels 6pk", "price": 9.09, "stock": 98, "aisle": "4A", "popularity": 71, "quality": "standard"},
    {"id": 178, "name": "Coles Bin Liners 50pk", "price": 8.24, "stock": 70, "aisle": "5E", "popularity": 82, "quality": "standard"},
    {"id": 179, "name": "Budget Dishwashing Liquid 1L", "price": 4.66, "stock": 0, "aisle": "4E", "popularity": 62, "quality": "premium"},
    {"id": 180, "name": "Homebrand All Purpose Cleaner 750ml", "price": 2.14, "stock": 0, "aisle": "2B", "popularity": 67, "quality": "premium"},
    {"id": 181, "name": "Organic Choice Toothpaste 120g", "price": 11.06, "stock": 0, "aisle": "4B", "popularity": 70, "quality": "standard"},
    {"id": 182, "name": "Coles Conditioner 400ml", "price": 24.59, "stock": 0, "aisle": "3A", "popularity": 64, "quality": "standard"},
    {"id": 183, "name": "Budget Shampoo 400ml", "price": 23.55, "stock": 0, "aisle": "5B", "popularity": 95, "quality": "premium"},
    {"id": 184, "name": "Coles Body Wash 1L", "price": 13.56, "stock": 0, "aisle": "5E", "popularity": 92, "quality": "budget"},
    {"id": 185, "name": "Coles Toothpaste 120g", "price": 23.23, "stock": 0, "aisle": "4E", "popularity": 83, "quality": "standard"},
    {"id": 186, "name": "Coles Toothbrush 2pk", "price": 4.69, "stock": 0, "aisle": "1E", "popularity": 64, "quality": "premium"},
    {"id": 187, "name": "Budget Conditioner 400ml", "price": 22.02, "stock": 0, "aisle": "2E", "popularity": 75, "quality": "budget"},
    {"id": 188, "name": "Homebrand Body Wash 1L", "price": 4.52, "stock": 15, "aisle": "3D", "popularity": 70, "quality": "budget"},
    {"id": 189, "name": "Budget Shampoo 400ml", "price": 7.87, "stock": 176, "aisle": "4B", "popularity": 78, "quality": "premium"},
    {"id": 190, "name": "Organic Choice Toothpaste 120g", "price": 4.47, "stock": 34, "aisle": "5E", "popularity": 60, "quality": "premium"},
    {"id": 191, "name": "FreshFarm Toothpaste 120g", "price": 2.47, "stock": 0, "aisle": "5A", "popularity": 63, "quality": "standard"},
    {"id": 192, "name": "Organic Choice Coles Hand Soap 250ml", "price": 4.49, "stock": 115, "aisle": "5C", "popularity": 94, "quality": "budget"},
    {"id": 193, "name": "FreshFarm Body Wash 1L", "price": 17.3, "stock": 81, "aisle": "2E", "popularity": 94, "quality": "budget"},
    {"id": 194, "name": "Organic Choice Deodorant 150ml", "price": 12.96, "stock": 0, "aisle": "3D", "popularity": 69, "quality": "budget"},
    {"id": 195, "name": "Organic Choice Conditioner 400ml", "price": 13.87, "stock": 0, "aisle": "3B", "popularity": 81, "quality": "budget"},
    {"id": 196, "name": "FreshFarm Shampoo 400ml", "price": 4.14, "stock": 171, "aisle": "2B", "popularity": 93, "quality": "budget"},
    {"id": 197, "name": "Coles Coles Hand Soap 250ml", "price": 5.2, "stock": 0, "aisle": "4A", "popularity": 73, "quality": "budget"},
    {"id": 198, "name": "Organic Choice Deodorant 150ml", "price": 3.72, "stock": 0, "aisle": "1A", "popularity": 76, "quality": "budget"},
    {"id": 199, "name": "Budget Body Wash 1L", "price": 2.99, "stock": 0, "aisle": "3E", "popularity": 88, "quality": "standard"},
    {"id": 200, "name": "Homebrand Toothpaste 120g", "price": 5.37, "stock": 0, "aisle": "3E", "popularity": 89, "quality": "premium"},
]

# Request/Response models
class RecommendationRequest(BaseModel):
    items: List[str]
    preference: str

@app.get("/")
def read_root():
    return {"message": "Smart Grocery List API"}

@app.post("/api/recommend")
async def get_recommendations(request: RecommendationRequest):
    try:
        # Verify API key is set
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured. Please set OPENAI_API_KEY in .env file")
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a smart grocery shopping assistant. You must respond ONLY with a JSON object containing an 'ids' array of product IDs."
                },
                {
                    "role": "user",
                    "content": f"""Given a list of items and shopping preference, recommend specific products from the database.

Items requested: {', '.join(request.items)}
Shopping preference: {request.preference}
Product Database: {json.dumps(PRODUCT_DATABASE)}

Recommend products based on the preference:
- budget, express: cheapest options with good stock
- quality: premium quality items or high popularity
- balanced: best overall value considering price, quality, stock

Return ONLY a JSON object with an 'ids' key containing an array of product IDs. Example: {{"ids": [1, 4, 10, 13]}}"""
                }
            ],
            temperature=0.7,
            max_tokens=500,
            response_format={"type": "json_object"}
        )

        # Parse response
        response_text = response.choices[0].message.content.strip()
        parsed = json.loads(response_text)
        # Extract IDs from response
        product_ids = parsed.get("ids", [])
        if not isinstance(product_ids, list):
            product_ids = list(parsed.values())[0] if parsed else []

        # Get full product details for recommended IDs
        recommended_products = [
            product for product in PRODUCT_DATABASE 
            if product["id"] in product_ids
        ]

        return {"products": recommended_products}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/api/products")
def get_products():
    return {"products": PRODUCT_DATABASE}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)