// Author: Dipika Rajput 11/11/2025
// sarveshdipika@gmail.com
import { ArrowLeft, ShoppingCart, Camera, DollarSign, Sparkles, Home, List, Package, ShoppingCart as CartIcon, Grid3x3 } from "lucide-react";
import { useState } from "react";
interface CreateNewListPageProps {
  onNavigate: (page: string) => void;
  currentTab: string;
  onTabChange: (tab: string) => void;
}
export function CreateNewListPage({ onNavigate, currentTab, onTabChange }: CreateNewListPageProps) {
  const [listItems, setListItems] = useState("Enter items or meals\n(one per line)\nmilk\nbread\neggs");
  const [preference, setPreference] = useState<'budget' | 'premium' | 'inspiration'>('budget');
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
        <div className="flex items-center gap-4">
          <button onClick={() => onNavigate('lists')}>
            <ArrowLeft className="w-6 h-6" />
          </button>
          <h1 className="text-xl">Create new list</h1>
        </div>
      </div>
      {/* Main Content */}
      <div className="flex-1 overflow-y-auto pb-20">
        {/* Header Section */}
        <div className="bg-white px-6 py-6 text-center border-b">
          <div className="flex justify-center mb-3">
            <div className="w-16 h-16 bg-red-600 rounded-2xl flex items-center justify-center">
              <ShoppingCart className="w-8 h-8 text-white" />
            </div>
          </div>
          <h2 className="text-2xl font-medium mb-2">Smart Grocery List</h2>
          <p className="text-gray-600">Shopping list recommendations</p>
        </div>
        {/* Your Shopping List Section */}
        <div className="px-4 py-6">
          <div className="bg-white rounded-2xl p-5 shadow-sm border border-gray-200">
            <div className="flex items-center gap-2 mb-4">
              <svg className="w-5 h-5 text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
              <h3 className="text-lg font-medium">Your Shopping List</h3>
            </div>
            <textarea
              value={listItems}
              onChange={(e) => setListItems(e.target.value)}
              className="w-full h-40 p-4 border-2 border-gray-300 rounded-xl resize-none outline-none focus:border-red-600 transition-colors text-gray-700"
              placeholder="Enter items or meals&#10;(one per line)"
            />
          </div>
        </div>
        {/* Upload Photo Section */}
        <div className="px-4 pb-6">
          <button className="w-full bg-white rounded-2xl p-8 shadow-sm border-2 border-dashed border-gray-300 hover:border-red-600 transition-colors">
            <div className="flex flex-col items-center gap-3">
              <div className="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center">
                <Camera className="w-8 h-8 text-gray-500" />
              </div>
              <p className="text-gray-600">Or upload a photo of your list</p>
            </div>
          </button>
        </div>
        {/* Shopping Preference Section */}
        <div className="px-4 pb-6">
          <div className="bg-white rounded-2xl p-6 shadow-sm border border-gray-200">
            <h3 className="text-xl mb-6 text-gray-800">Shopping Preference</h3>
            {/* Budget and Premium Row */}
            <div className="grid grid-cols-2 gap-4 mb-4">
              {/* Budget Option */}
              <button
                onClick={() => setPreference('budget')}
                className={`p-6 rounded-2xl transition-all ${
                  preference === 'budget'
                    ? 'bg-red-50 ring-2 ring-red-600'
                    : 'bg-gray-100 hover:bg-gray-200'
                }`}
              >
                <div className="flex flex-col items-center gap-3">
                  <DollarSign className={`w-10 h-10 ${
                    preference === 'budget' ? 'text-red-600' : 'text-gray-700'
                  }`} strokeWidth={2} />
                  <span className={`font-medium text-lg ${
                    preference === 'budget' ? 'text-red-600' : 'text-gray-800'
                  }`}>Budget</span>
                  <span className="text-sm text-gray-500">Best prices</span>
                </div>
              </button>
              {/* Premium Option */}
              <button
                onClick={() => setPreference('premium')}
                className={`p-6 rounded-2xl transition-all ${
                  preference === 'premium'
                    ? 'bg-red-50 ring-2 ring-red-600'
                    : 'bg-gray-100 hover:bg-gray-200'
                }`}
              >
                <div className="flex flex-col items-center gap-3">
                  <svg className={`w-10 h-10 ${preference === 'premium' ? 'text-red-600' : 'text-gray-700'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                  <span className={`font-medium text-lg ${
                    preference === 'premium' ? 'text-red-600' : 'text-gray-800'
                  }`}>Premium</span>
                  <span className="text-sm text-gray-500">Top quality</span>
                </div>
              </button>
            </div>
            {/* Inspiration Option - Full Width */}
            <button
              onClick={() => setPreference('inspiration')}
              className={`w-full p-6 rounded-2xl transition-all ${
                preference === 'inspiration'
                  ? 'bg-red-50 ring-2 ring-red-600'
                  : 'bg-gray-100 hover:bg-gray-200'
              }`}
            >
              <div className="flex flex-col items-center gap-3">
                <svg className={`w-10 h-10 ${preference === 'inspiration' ? 'text-red-600' : 'text-gray-700'}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                </svg>
                <span className={`font-medium text-lg ${
                  preference === 'inspiration' ? 'text-red-600' : 'text-gray-800'
                }`}>Inspiration</span>
                <span className="text-sm text-gray-500">Inspiration Suggestions</span>
              </div>
            </button>
          </div>
        </div>
        {/* Generate List Button */}
        <div className="px-4 pb-8">
          <button
            onClick={() => {
              alert('Generating your smart grocery list...');
              onNavigate('my-list-detail');
            }}
            className="w-full bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-2xl py-5 font-medium hover:from-purple-700 hover:to-blue-700 transition-all shadow-lg flex items-center justify-center gap-3"
          >
            <Sparkles className="w-6 h-6" />
            <span className="text-lg">Create Smart Trolley from List</span>
          </button>
        </div>
      </div>
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
            <CartIcon className="w-6 h-6" />
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