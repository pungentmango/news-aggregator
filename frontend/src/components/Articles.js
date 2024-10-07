import React from 'react';
import { AiOutlineExport } from 'react-icons/ai';
import Loading from './Loading';

const Articles = ({ articles }) => {
    if (!articles || articles.length === 0) {
        return <Loading/>
    }

    // Function to format the publish date
    const formatDate = (dateString) => {
        const date = new Date(dateString);
        // Check if the date is valid
        if (isNaN(date.getTime())) {
            return null; // Return null if the date is invalid
        }
        // Format the date and time
        return date.toLocaleString(); // Formats date to "MM/DD/YYYY, HH:MM:SS AM/PM"
    };

    return (
        <div className="flex flex-col space-y-4 mt-4">
            {articles.map((article, index) => (
                <div
                    key={index}
                    className="relative border p-4 rounded-lg shadow hover:shadow-lg transition duration-200"
                >
                    {/* Article Title */}
                    <h2 className="text-lg font-bold cursor-pointer" onClick={() => window.open(article.link, "_blank")}>
                        {article.title}
                    </h2>

                    {/* Icon to indicate new tab */}
                    <a
                        href={article.link}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="absolute top-2 right-2 text-gray-600 hover:text-gray-800"
                        title="Open in new tab"
                    >
                        <AiOutlineExport className="text-lg" />
                    </a>

                    {/* Article Description */}
                    <p className="mt-2">{article.description}</p>

                    {/* Publish Date */}
                    <p className="text-sm text-gray-500 text-right mt-4">
                        {formatDate(article.published) || "Publish date not available"}
                    </p>
                </div>
            ))}
        </div>
    );
};

export default Articles;
