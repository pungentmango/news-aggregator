// src/components/News.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
    const [newsData, setNewsData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await axios.get('http://localhost:5000/news');
                setNewsData(response.data);
                setLoading(false);
            } catch (err) {
                setError(err);
                setLoading(false);
            }
        };

        fetchNews();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error fetching news: {error.message}</div>;
    }

    return (
        <div>
            <h1>News Aggregator</h1>
            {Object.keys(newsData).map((category) => (
                <div key={category}>
                    <h2>{category.charAt(0).toUpperCase() + category.slice(1)}</h2>
                    <ul>
                        {newsData[category].map((article, index) => (
                            <li key={index}>
                                <a href={article.link} target="_blank" rel="noopener noreferrer">
                                    {article.title}
                                </a>
                                <p>{article.description}</p>
                                <small>
                                    Published on: {article.published} by {article.creator}
                                </small>
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
};

export default News;
