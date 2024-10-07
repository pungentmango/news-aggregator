import React, { useState, useEffect } from 'react';
import axios from 'axios';

import Articles from './Articles';
import Header from './Header';

const News = () => {
    const [activeTab, setActiveTab] = useState('');
    const [tabs, setTabs] = useState([]);
    const [newsData, setNewsData] = useState({});
  
    // Fetch news based on the active tab
    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await axios.get(`http://localhost:5000/news`);
                setNewsData(response.data);
                const fetchedTabs = Object.keys(response.data);
                setTabs(fetchedTabs);
                
                // Set the active tab to the first one if available
                if (fetchedTabs.length > 0) {
                    setActiveTab(fetchedTabs[0]);
                }
            } catch (error) {
                console.error('Error fetching news:', error);
            }
        };
  
        fetchNews();
    }, []);  

    return (
        <div className='w-full'>
            <Header siteName="News Aggregator" tabs={tabs} activeTab={activeTab} setActiveTab={setActiveTab} />
            <Articles articles={newsData[activeTab]} />
        </div>
    );
};

export default News;
