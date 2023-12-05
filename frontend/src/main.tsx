import React from 'react'
import ReactDOM from 'react-dom/client'
import {
    createBrowserRouter,
    RouterProvider,
  } from "react-router-dom";
import './index.css'
import App from './App.tsx'
import Main from './pages/Main/index.tsx';
import Sight from './pages/Sight/index.tsx';

const router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
        children: [
            {
                path: '',
                element: <Main />
            },
            {
                path: 'sight/:id',
                loader: ({params}) => {
                    if (!params.id) return null
                    return params.id
                },
                element: <Sight />
            }
        ]
    }
])

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <RouterProvider router={router}/>
    </React.StrictMode>,
)
