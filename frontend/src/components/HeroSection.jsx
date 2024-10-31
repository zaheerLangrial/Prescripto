import React, { useEffect, useState } from 'react';
import HeroSectionPic from '../assets/doc-header-img.jpg';
import { ArrowRightOutlined } from '@ant-design/icons';

const HeroSection = () => {
  const [heroData, setHeroData] = useState(null);
  const [loading, setLoading] = useState(true);
  console.log('heroData ===>', heroData)

  useEffect(() => {
    fetch('http://localhost:8005/herosection/')
      .then((response) => response.json())
      .then((data) => {
        setHeroData(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching hero data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="bg-[#5F6FFF] flex items-center pt-16 px-20 mt-6">
      <div className="flex-1">
        <h1 className="text-white font-outfit text-[63px] font-semibold leading-[80px] text-left">
          {heroData?.title}
        </h1>
        <button className="mt-8 bg-white text-[#5F6FFF] font-semibold px-8 py-4 rounded-full flex items-center space-x-3 shadow-lg hover:bg-gray-100 transition">
          <span>{heroData?.buttonText}</span>
          <ArrowRightOutlined className="text-xl" />
        </button>
      </div>
      <div className="flex-1 bg-transparent">
        <img
          src={HeroSectionPic}
          alt="Doctors"
          className="w-full h-auto object-cover bg-transparent"
        />
      </div>
    </div>
  );
};

export default HeroSection;
