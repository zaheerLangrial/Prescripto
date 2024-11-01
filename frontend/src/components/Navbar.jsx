import React, { useEffect, useState } from 'react';
import { Button, Skeleton, Modal, Form, Input, Select, Upload, message } from 'antd';
import { UploadOutlined } from '@ant-design/icons';

const { Option } = Select;

const Navbar = () => {
  const [navbarItems, setNavbarItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [role, setRole] = useState('');
  const [categories, setCategories] = useState([]);
  const [loadingCategories, setLoadingCategories] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [fileList, setFileList] = useState([]); // State for file uploads

  useEffect(() => {
    // Fetch navbar items
    fetch('http://localhost:8005/navbar/')
      .then((response) => response.json())
      .then((data) => {
        setNavbarItems(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching navbar:', error);
        setLoading(false);
      });

    // Fetch categories
    fetch('http://localhost:8005/categories/')
      .then((response) => response.json())
      .then((data) => {
        setCategories(data);
        setLoadingCategories(false);
      })
      .catch((error) => {
        console.error('Error fetching categories:', error);
        setLoadingCategories(false);
      });
  }, []);

  const showModal = () => {
    setIsModalVisible(true);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  const onFinish = async (values) => {
    const formData = new FormData();
    formData.append('name', values.username);
    formData.append('role', role);
    formData.append('category', selectedCategory);
    formData.append('experience', values.experience); // Include experience
    formData.append('image', fileList[0]?.originFileObj); // Use originFileObj to get the file

    console.log('formdata ----> ', formData)
  };


  const handleRoleChange = (value) => {
    setRole(value);
  };

  const handleCategoryChange = (value) => {
    setSelectedCategory(value); // Update selected category
  };

  return (
    <nav className="flex items-center justify-between p-4 bg-blue-600 shadow-md">
      <div className="text-white text-2xl font-bold">Prescripto</div>

      <ul className="flex space-x-8">
        {loading ? (
          Array(3)
            .fill(0)
            .map((_, index) => (
              <li key={index}>
                <Skeleton.Input active size="small" style={{ width: 80 }} />
              </li>
            ))
        ) : (
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

      <Button type="primary" size="large" onClick={showModal} className="bg-green-500 hover:bg-green-600">
        {loading ? <Skeleton.Button active size="small" /> : 'Create Account'}
      </Button>

      <Modal
        title="Create Account"
        visible={isModalVisible}
        onCancel={handleCancel}
        footer={null}
      >
        <Form
          layout="vertical"
          onFinish={onFinish}
          initialValues={{ role: '', experience: '' }}
        >
          <Form.Item
            name="username"
            label="Username"
            rules={[{ required: true, message: 'Please enter your username!' }]}
          >
            <Input placeholder="Enter your username" />
          </Form.Item>

          <Form.Item
            name="profilePic"
            label="Profile Picture"
            valuePropName="fileList"
            getValueFromEvent={(e) => {
              setFileList(e.fileList); // Save the file in state
              return e.fileList;
            }}
          >
            <Upload
              listType="picture"
              beforeUpload={() => false}
              onChange={({ fileList: newFileList }) => setFileList(newFileList)} // Set file list here
            >
              <Button icon={<UploadOutlined />}>Upload Profile Picture</Button>
            </Upload>

          </Form.Item>

          <Form.Item
            name="role"
            label="Role"
            rules={[{ required: true, message: 'Please select a role!' }]}
          >
            <Select placeholder="Select your role" onChange={handleRoleChange}>
              <Option value="doctor">Doctor</Option>
              <Option value="patient">Patient</Option>
            </Select>
          </Form.Item>

          {role === 'doctor' && (
            <>
              <Form.Item
                name="category"
                label="Category"
                rules={[{ required: true, message: 'Please select your category!' }]}
              >
                <Select placeholder="Select doctor category" onChange={handleCategoryChange}>
                  {loadingCategories ? (
                    <Option value="" disabled>
                      Loading categories...
                    </Option>
                  ) : (
                    categories.map((category) => (
                      <Option key={category.id} value={category.id}>
                        {category.name}
                      </Option>
                    ))
                  )}
                </Select>
              </Form.Item>

              <Form.Item
                name="experience"
                label="Experience (Years)"
                rules={[{ required: role === 'doctor', message: 'Please enter your experience!' }]}
              >
                <Input placeholder="Enter years of experience" />
              </Form.Item>
            </>
          )}

          <Form.Item>
            <Button type="primary" htmlType="submit" className="w-full">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </Modal>
    </nav>
  );
};

export default Navbar;
