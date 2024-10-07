import React, { useState } from 'react';
import { AiOutlineMenu } from 'react-icons/ai'; // Importing hamburger icon
import { AiOutlineClose } from 'react-icons/ai'; // Importing close icon

const Header = ({ tabs, activeTab, setActiveTab, siteName }) => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    return (
        <header className="bg-gray-800 text-white py-4 w-full">
            <div className="container mx-auto flex justify-between items-center">
                {/* Logo and Site Name */}
                <div className="flex items-center space-x-3">
                    <h1 className="text-xl font-bold px-4">{siteName}</h1>
                </div>

                {/* Hamburger Icon */}
                <div className="block md:hidden">
                    <button onClick={toggleMenu} className="px-4 focus:outline-none">
                        {isMenuOpen ? (
                            <AiOutlineClose className="text-2xl" />
                        ) : (
                            <AiOutlineMenu className="text-2xl" />
                        )}
                    </button>
                </div>

                {/* Tabs */}
                <nav className={`md:block ${isMenuOpen ? 'block' : 'hidden'} z-10 md:flex md:space-x-6 absolute md:static bg-gray-800 left-0 right-0 top-16 md:top-auto md:bg-transparent`}>
                    <div className="flex flex-col md:flex-row md:space-x-6">
                        {tabs.map((type) => (
                            <button
                                key={type}
                                onClick={() => {
                                    setActiveTab(type);
                                    setIsMenuOpen(false); // Close the menu when a tab is selected
                                }}
                                className={`px-4 py-2 text-sm font-medium focus:outline-none
                                    ${activeTab === type
                                        ? 'text-white bg-slate-600 rounded-lg'
                                        : 'text-gray-600 hover:bg-slate-200 hover:text-slate-800 rounded-lg'
                                    }`}
                            >
                                {type.charAt(0).toUpperCase() + type.slice(1)}
                            </button>
                        ))}
                    </div>
                </nav>
            </div>
        </header>
    );
};

export default Header;
