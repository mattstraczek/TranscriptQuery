import React from 'react'
import { Link } from "react-router-dom";

function Header({ title }) {
    return (
      <nav className="navbar mb-12 shadow-lg bg-blue-700 text-neutral-content">
        <div className="container mx-auto">
          <div className="flex-none px-8 mx-8"></div>
          <h2 className="text-2xl m-2">
            <Link to="/" className="font-thin">
              {title}
            </Link>
          </h2>
        </div>
        <div className="flex-1 px-2 mx-2">
          <div className="flex justify-end">
          <Link to="/" className="btn btn-ghost btn-sm rounded-btn">
              Query Search
            </Link>
          <Link to="/SearchEngine" className="btn btn-ghost btn-sm rounded-btn">
              Search Engine
            </Link>
          </div>
        </div>
      </nav>
    );

} export default Header;