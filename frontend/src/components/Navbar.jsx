import React, { useEffect, useState } from 'react';
import { Button, Skeleton } from 'antd';

const Navbar = () => {
  const [navbarItems, setNavbarItems] = useState([]);
  const [loading, setLoading] = useState(true); // Track loading state

  useEffect(() => {
    fetch('http://localhost:8005/navbar/')
      .then((response) => response.json())
      .then((data) => {
        setNavbarItems(data);
        setLoading(false); // Stop loading once data is fetched
      })
      .catch((error) => {
        console.error('Error fetching navbar:', error);
        setLoading(false); // Stop loading even if an error occurs
      });
  }, []);

  return (
    <nav className="flex items-center justify-between p-4 bg-blue-600 shadow-md">
      {/* Left Section: Website Name */}
      <div className="text-white text-2xl font-bold">Prescripto</div>

      {/* Middle Section: Navbar Items with Skeleton */}
      <ul className="flex space-x-8">
        {loading ? (
          // Show Skeletons while loading
          Array(3)
            .fill(0)
            .map((_, index) => (
              <li key={index}>
                <Skeleton.Input active size="small" style={{ width: 80 }} />
              </li>
            ))
        ) : (
          // Render fetched navbar items
          navbarItems.map((item) => (
            <li key={item.id}>
              <a
                href={item.url}
                className="text-white hover:text-gray-300 text-lg"
              >
                {item.title}
              </a>
            </li>
          ))
        )}
      </ul>

      {/* Right Section: Create Account Button */}
      <Button type="primary" size='large' className="bg-green-500 hover:bg-green-600">
        {loading ? <Skeleton.Button active size="small" /> : 'Create Account'}
      </Button>
    </nav>
  );
};

export default Navbar;
