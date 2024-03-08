import React from 'react'
import './Nav.css';
import { Outlet,Link, useLocation } from 'react-router-dom';

function Nav() {
    const location = useLocation();
    return (
    <>
        <nav>
            <ul>
                <li ><Link to="/" className={location.pathname === '/' ? 'active' : ''} >Home</Link></li>
                <li><Link  to="/asistencia" className={location.pathname === '/asistencia' ? 'active' : ''}>Asistencia </Link></li>
                <li><Link  to="/EstudentForm" className={location.pathname === '/estudiante' ? 'active' : ''}>Estudiante </Link></li>
                <li style={{float:"right"}}><a  href="#about">Usuario</a></li>
            </ul>
        </nav>
        <Outlet />
    </>
    )
}

export default Nav