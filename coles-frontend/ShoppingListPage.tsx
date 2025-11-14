// Author: Dipika Rajput 11/11/2025
// sarveshdipika@gmail.com
import { Search, MoreVertical, Plus, Home, List, Package, ShoppingCart, Grid3x3 } from "lucide-react";
import { useState } from "react";
interface ListsOverviewPageProps {
  onNavigate: (page: string) => void;
  currentTab: string;
  onTabChange: (tab: string) => void;
}
export function ListsOverviewPage({ onNavigate, currentTab, onTabChange }: ListsOverviewPageProps) {
  const [activeTab, setActiveTab] = useState<'my-lists' | 'suggested'>('my-lists');
  return (
    <div className="flex flex-col h-screen bg-gray-50 max-w-md mx-auto">
      {/* Status Bar */}
      <div className="bg-white px-4 py-2 flex items-center justify-between text-sm">
        <span>6:21</span>
        <div className="flex items-center gap-2">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-gray-600">
            <path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3c-1.65-1.66-4.34-1.66-6 0zm-4-4l2 2c2.76-2.76 7.24-2.76 10 0l2-2C15.14 9.14 8.87 9.14 5 13z"/>
          </svg>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-gray-600">
            <rect x="1" y="5" width="22" height="14" rx="2" />
          </svg>
        </div>
      </div>
      {/* Header */}
      <div className="bg-white px-4 py-4 flex items-center justify-between border-b">
        <h1 className="text-2xl font-medium">Lists</h1>
        <button onClick={() => alert('Search lists...')}>
          <Search className="w-6 h-6" />
        </button>
      </div>
      {/* Tabs */}
      <div className="bg-white flex border-b">
        <button
          onClick={() => setActiveTab('my-lists')}
          className={`flex-1 py-3 text-center font-medium relative ${
            activeTab === 'my-lists' ? 'text-red-600' : 'text-gray-600'
          }`}
        >
          My lists
          {activeTab === 'my-lists' && (
            <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-red-600"></div>
          )}
        </button>
        <button
          onClick={() => setActiveTab('suggested')}
          className={`flex-1 py-3 text-center font-medium relative ${
            activeTab === 'suggested' ? 'text-red-600' : 'text-gray-600'
          }`}
        >
          Suggested
          {activeTab === 'suggested' && (
            <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-red-600"></div>
          )}
        </button>
      </div>
      {/* Main Content */}
      <div className="flex-1 overflow-y-auto pb-20">
        {activeTab === 'my-lists' ? (
          <div className="p-4 space-y-4">
            {/* Log in or sign up Card */}
            <div className="bg-gray-900 rounded-2xl p-5 text-white flex items-center justify-between">
              <div className="flex-1">
                <h3 className="font-medium mb-1">Log in or sign up</h3>
                <p className="text-sm text-gray-300">To create lists and view all your saved items.</p>
              </div>
              <div className="w-10 h-10 rounded-lg border-2 border-white flex items-center justify-center ml-3">
                <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
            </div>
            {/* My list Card */}
            <button
              onClick={() => onNavigate('my-list-detail')}
              className="w-full bg-white rounded-2xl p-5 shadow-sm border border-gray-200 flex items-center justify-between hover:shadow-md transition-shadow"
            >
              <div className="text-left">
                <h3 className="font-medium text-lg mb-1">My list</h3>
                <p className="text-sm text-gray-500">0 items</p>
              </div>
              <div className="w-10 h-10 rounded-full border-2 border-gray-900 flex items-center justify-center">
                <MoreVertical className="w-5 h-5" />
              </div>
            </button>
          </div>
        ) : (
          <div className="p-4">
            <p className="text-center text-gray-500 mt-8">No suggested lists available</p>
          </div>
        )}
      </div>
      {/* Create a new list Button */}
      <button
        onClick={() => onNavigate('create-new-list')}
        className="fixed bottom-20 right-4 max-w-md bg-red-600 text-white rounded-full px-6 py-4 shadow-lg flex items-center gap-2 hover:bg-red-700 transition-colors"
      >
        <Plus className="w-5 h-5" />
        <span className="font-medium">Create a new list</span>
      </button>
      {/* Bottom Navigation */}
      <div className="fixed bottom-0 left-0 right-0 max-w-md mx-auto bg-white border-t">
        <div className="flex items-center justify-around px-2 py-2">
          <button
            onClick={() => onTabChange('home')}
            className={`flex flex-col items-center py-2 px-4 transition-colors ${
              currentTab === 'home' ? 'text-red-600' : 'text-gray-600'
            }`}
          >
            <Home className="w-6 h-6" />
            <span className="text-xs mt-1">Home</span>
          </button>
          <button
            onClick={() => onTabChange('lists')}
            className={`flex flex-col items-center py-2 px-4 transition-colors ${
              currentTab === 'lists' ? 'text-red-600' : 'text-gray-600'
            }`}
          >
            <List className="w-6 h-6" />
            <span className="text-xs mt-1">Lists</span>
          </button>
          <button
            onClick={() => onTabChange('products')}
            className={`flex flex-col items-center py-2 px-4 transition-colors ${
              currentTab === 'products' ? 'text-red-600' : 'text-gray-600'
            }`}
          >
            <Package className="w-6 h-6" />
            <span className="text-xs mt-1">Products</span>
          </button>
          <button
            onClick={() => onTabChange('trolley')}
            className={`flex flex-col items-center py-2 px-4 transition-colors ${
              currentTab === 'trolley' ? 'text-red-600' : 'text-gray-600'
            }`}
          >
            <ShoppingCart className="w-6 h-6" />
            <span className="text-xs mt-1">Trolley</span>
          </button>
          <button
            onClick={() => onTabChange('more')}
            className={`flex flex-col items-center py-2 px-4 transition-colors ${
              currentTab === 'more' ? 'text-red-600' : 'text-gray-600'
            }`}
          >
            <Grid3x3 className="w-6 h-6" />
            <span className="text-xs mt-1">More</span>
          </button>
        </div>
      </div>
    </div>
  );
}