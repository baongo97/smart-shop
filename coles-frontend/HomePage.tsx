// Author: Dipika Rajput 11/11/2025
// sarveshdipika@gmail.com
import { Search, MapPin, List, Home, Package, ShoppingCart, Grid3x3, ScanBarcode, User } from "lucide-react";
import { ImageWithFallback } from "./figma/ImageWithFallback";
interface HomePageProps {
  onNavigate: (page: string) => void;
  currentTab: string;
  onTabChange: (tab: string) => void;
}
export function HomePage({ onNavigate, currentTab, onTabChange }: HomePageProps) {
  return (
    <div className="flex flex-col h-screen bg-white max-w-md mx-auto">
      {/* Status Bar */}
      <div className="bg-white px-4 py-2 flex items-center justify-between text-sm">
        <span>5:22</span>
        <div className="flex items-center gap-2">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-gray-600">
            <path d="M1 9l2 2c4.97-4.97 13.03-4.97 18 0l2-2C16.93 2.93 7.08 2.93 1 9zm8 8l3 3 3-3c-1.65-1.66-4.34-1.66-6 0zm-4-4l2 2c2.76-2.76 7.24-2.76 10 0l2-2C15.14 9.14 8.87 9.14 5 13z"/>
          </svg>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-gray-600">
            <rect x="1" y="5" width="22" height="14" rx="2" />
          </svg>
        </div>
      </div>
      {/* Delivery Type Tabs */}
      <div className="flex gap-2 px-4 py-3">
        <button className="px-6 py-2.5 bg-black text-white rounded-full text-sm">In store</button>
        <button className="px-6 py-2.5 bg-white text-black rounded-full text-sm border border-gray-300">Click & Collect</button>
        <button className="px-6 py-2.5 bg-white text-black rounded-full text-sm border border-gray-300">Delivery</button>
      </div>
      {/* Store Location and Find Item */}
      <div className="flex items-center justify-between px-4 py-3 border-b">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-red-600" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
          </svg>
          <span>Coles Burwood East</span>
        </div>
        <button
          className="flex items-center gap-2 text-red-600 hover:text-red-700 transition-colors"
          onClick={() => alert('Opening Find Item in Store...')}
        >
          <MapPin className="w-5 h-5" />
          <span className="text-sm font-medium">Find Item in Store</span>
        </button>
      </div>
      {/* Search Bar */}
      <div className="px-4 py-3">
        <div className="flex items-center gap-3 border-2 border-gray-300 rounded-full px-4 py-3">
          <Search className="w-5 h-5 text-gray-500" />
          <input
            type="text"
            placeholder="Search for products"
            className="flex-1 outline-none text-sm"
          />
          <ScanBarcode className="w-5 h-5 text-gray-500" />
        </div>
      </div>
      {/* Main Content */}
      <div className="flex-1 overflow-y-auto pb-20">
        {/* Log in or sign up Card */}
        <div className="px-4 py-3">
          <div className="border border-gray-300 rounded-2xl p-5 flex items-center justify-between">
            <div>
              <h3 className="font-medium mb-1">Log in or sign up</h3>
              <p className="text-sm text-gray-600">Place orders, save lists, link Flybuys and more.</p>
            </div>
            <div className="w-10 h-10 rounded-full border-2 border-gray-900 flex items-center justify-center">
              <User className="w-5 h-5" />
            </div>
          </div>
        </div>
        {/* Browse Products */}
        <div className="px-4 py-4">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg">Browse products</h2>
            <button className="text-red-600 text-sm">View all</button>
          </div>
          <div className="flex gap-6 overflow-x-auto pb-2">
            {/* Bought before */}
            <div className="flex flex-col items-center gap-2 min-w-[70px]">
              <div className="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center text-white">
                <span className="text-lg">BB</span>
              </div>
              <span className="text-xs text-center">Bought<br/>before</span>
            </div>
            {/* Christmas */}
            <div className="flex flex-col items-center gap-2 min-w-[70px]">
              <div className="w-16 h-16 rounded-full flex items-center justify-center">
                <ImageWithFallback
                  src="https://images.unsplash.com/photo-1702141258459-6dd8f817e79a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxjaHJpc3RtYXMlMjBkZWNvcmF0aW9uc3xlbnwxfHx8fDE3NjI2Nzk2MTR8MA&ixlib=rb-4.1.0&q=80&w=1080"
                  alt="Christmas"
                  className="w-16 h-16 rounded-full object-cover"
                />
              </div>
              <span className="text-xs text-center">Christmas</span>
            </div>
            {/* Down Down */}
            <div className="flex flex-col items-center gap-2 min-w-[70px]">
              <div className="w-16 h-16 rounded-full border-4 border-red-600 flex items-center justify-center bg-white">
                <div className="text-center leading-tight">
                  <div className="text-[9px] font-bold text-red-600">DOWN</div>
                  <div className="text-[9px] font-bold text-red-600">DOWN</div>
                </div>
              </div>
              <span className="text-xs text-center">Down<br/>Down</span>
            </div>
            {/* Meat & Seafood */}
            <div className="flex flex-col items-center gap-2 min-w-[70px]">
              <div className="w-16 h-16 rounded-full flex items-center justify-center">
                <ImageWithFallback
                  src="https://images.unsplash.com/photo-1607623814075-e51df1bdc82f?w=100&h=100&fit=crop"
                  alt="Meat & Seafood"
                  className="w-16 h-16 rounded-full object-cover"
                />
              </div>
              <span className="text-xs text-center">Meat &<br/>Seafood</span>
            </div>
            {/* Fruit & Vegetables */}
            <div className="flex flex-col items-center gap-2 min-w-[70px]">
              <div className="w-16 h-16 rounded-full flex items-center justify-center">
                <ImageWithFallback
                  src="https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=100&h=100&fit=crop"
                  alt="Fruit & Vegetables"
                  className="w-16 h-16 rounded-full object-cover"
                />
              </div>
              <span className="text-xs text-center">Fruit &<br/>Vegetables</span>
            </div>
          </div>
        </div>
        {/* Black Friday Promotional Banner */}
        <div className="px-4 py-3">
          <div className="bg-gradient-to-br from-gray-900 to-gray-800 rounded-2xl p-5 text-white relative overflow-hidden">
            <div className="absolute top-2 right-2 text-4xl opacity-20">:tada:</div>
            <div className="flex items-start gap-4">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-2">
                  <div className="bg-red-600 text-white px-2 py-1 rounded text-xs font-bold">Black Friday</div>
                  <div className="bg-red-600 text-white px-2 py-1 rounded text-xs font-bold">Rewards Week</div>
                </div>
                <h3 className="font-medium mb-2">Black Friday Rewards Week starts now</h3>
                <p className="text-sm text-gray-300">Shop online and score bonus Flybuys points this week.</p>
              </div>
            </div>
          </div>
        </div>
        {/* Second Promotional Banner */}
        <div className="px-4 py-3">
          <div className="bg-gradient-to-br from-blue-900 to-blue-800 rounded-2xl p-5 text-white flex items-center justify-between">
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-2">
                <div className="bg-blue-400 rounded-full px-3 py-1">
                  <span className="text-sm font-bold">Flybuys</span>
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-1">8,000</h3>
              <p className="text-sm text-gray-300">bonus points</p>
            </div>
            <div className="text-4xl">:credit_card:</div>
          </div>
        </div>
        {/* Log in or sign up Button */}
        <div className="px-4 py-4 pb-8">
          <button className="w-full bg-red-600 text-white rounded-full py-4 flex items-center justify-center gap-2 font-medium hover:bg-red-700 transition-colors">
            <User className="w-5 h-5" />
            Log in or sign up
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