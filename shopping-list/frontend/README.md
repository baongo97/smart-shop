# Smart Shopping Frontend
### by **Gia Bao Ngo**  
📧 ngbao128@gmail.com

A React-based web application that transforms a customer's **handwritten shopping list**, **dietary information** (gluten-free, nut allergy, vegan), and **shopping preferences** (budget, premium, inspiration) into a fully structured shopping list generated using the **OpenAI API**, mapped to **real products** in the database.

---

## 🚀 Features

### ✍️ Handwritten List Recognition
- Upload or capture a photo of a handwritten shopping list.
- The system extracts items using OpenAI Vision models.

### 🥗 Dietary & Allergy Considerations
Users can specify:
- Gluten-free  
- Nut allergy  
- Vegan  
The AI automatically adjusts product selections to match restrictions.

### 💸 Shopping Preferences
Choose between:
- **Budget** – cost-optimized suggestions  
- **Premium** – high-quality or organic options  
- **Inspiration** – creative, curated recommendations  

### 🤖 AI-Generated Shopping List
- Uses OpenAI API to interpret the handwritten list.
- Matches extracted items to **real products** in the product database.
- Generates quantity suggestions, alternatives, and optimized selections.

---

## How to run
```bash
# install
npm install

# start (common scripts)
npm start      # production/start script
npm run dev    # development
# tests
npm test
```
Open browser at http://localhost:5173 or the port shown in logs.