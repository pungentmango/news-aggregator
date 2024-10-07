import React from 'react';

const Loading = () => {
    return (
        <div className="flex justify-center items-center flex-col pt-16">
            <div className="loader"></div>
            <p className="text-lg text-gray-600">Loading...</p>
        </div>
    );
};

export default Loading;
