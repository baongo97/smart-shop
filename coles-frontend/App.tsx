// Author: Dipika Rajput 11/11/2025
// sarveshdipika@gmail.com
import { ShoppingListPage } from "./components/ShoppingListPage";
import { HomePage } from "./components/HomePage";
import { ListsOverviewPage } from "./components/ListsOverviewPage";
import { CreateNewListPage } from "./components/CreateNewListPage";
import { useState } from "react";
export default function App() {
  const [currentPage, setCurrentPage] = useState("home");
  const [currentTab, setCurrentTab] = useState("home");
  const handleNavigate = (page: string) => {
    setCurrentPage(page);
    // Update tab only if navigating to a main tab page
    if (['home', 'lists', 'products', 'trolley', 'more'].includes(page)) {
      setCurrentTab(page);
    }
  };
  const handleTabChange = (tab: string) => {
    setCurrentTab(tab);
    setCurrentPage(tab);
  };
  // Home Page
  if (currentPage === "home") {
    return <HomePage onNavigate={handleNavigate} currentTab={currentTab} onTabChange={handleTabChange} />;
  }
  // Lists Overview Page
  if (currentPage === "lists") {
    return <ListsOverviewPage onNavigate={handleNavigate} currentTab={currentTab} onTabChange={handleTabChange} />;
  }
  // Create New List Page
  if (currentPage === "create-new-list") {
    return <CreateNewListPage onNavigate={handleNavigate} currentTab={currentTab} onTabChange={handleTabChange} />;
  }
  // My List Detail Page
  if (currentPage === "my-list-detail") {
    return <ShoppingListPage onNavigate={handleNavigate} currentTab={currentTab} onTabChange={handleTabChange} />;
  }
  // Default to home page
  return <HomePage onNavigate={handleNavigate} currentTab={currentTab} onTabChange={handleTabChange} />;
}