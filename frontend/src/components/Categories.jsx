import { useState, useEffect } from "react";
import { Card, Badge } from "antd";
import axios from "axios";

const Categories = () => {
  const [categories, setCategories] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);

  // Fetch categories from backend
  useEffect(() => {
    axios
      .get("http://localhost:8005/categories/")
      .then((response) =>
        setCategories([{ id: null, name: "All", icon: "🌍" }, ...response.data]) // Add "All" category
      )
      .catch((error) => console.error(error));
  }, []);

  // Fetch doctors based on selected category
  useEffect(() => {
    const categoryParam = selectedCategory ? `?category=${selectedCategory}` : "";
    axios
      .get(`http://localhost:8005/doctors/${categoryParam}`)
      .then((response) => setDoctors(response.data))
      .catch((error) => console.error(error));
  }, [selectedCategory]);

  return (
    <div className="p-6">
      {/* Category Buttons */}
      <div className="flex justify-center gap-6 mb-8">
        {categories.map((category) => (
          <div
            key={category.id}
            onClick={() => setSelectedCategory(category.id)}
            className="flex flex-col items-center cursor-pointer"
          >
            <div
              className={`flex items-center justify-center w-20 h-20 rounded-full 
                ${selectedCategory === category.id ? "bg-green-500" : "bg-blue-500"}
                text-white hover:bg-blue-700 transition`}
            >
              <span className="text-2xl">{category.icon}</span>
            </div>
            <span className="mt-2 text-sm text-center">{category.name}</span>
          </div>
        ))}
      </div>

      {/* Doctor Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {doctors.map((doctor) => (
          <Card
            key={doctor.id}
            title={
              <Badge
                status={doctor.is_active ? "success" : "error"}
                text={doctor.is_active ? "Active" : "Inactive"}
              />
            }
            className="shadow-md"
          >
            <img
              src={doctor.image}
              alt={doctor.name}
              className="w-full h-40 object-cover rounded mb-2"
            />
            <p>{doctor.name}</p>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Categories;
