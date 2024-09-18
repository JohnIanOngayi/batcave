import { Outlet } from "react-router-dom";
import NavBar from "../components/Navbar";
import Navbar from "../components/Navbar";

const MainLayout = () => {
  return (
    <>
      <Navbar />
      <Outlet />
    </>
  );
};

export default MainLayout;
