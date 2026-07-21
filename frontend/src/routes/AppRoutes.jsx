import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "../layout/MainLayout";

import Dashboard from "../pages/Dashboard";
import Upload from "../pages/Upload";
import Forecast from "../pages/Forecast";
import History from "../pages/History";
import About from "../pages/About";
import NotFound from "../pages/NotFound";


function AppRoutes(){

return(

<BrowserRouter>

<MainLayout>

<Routes>

<Route 
path="/" 
element={<Dashboard/>}
/>


<Route 
path="/upload" 
element={<Upload/>}
/>


<Route 
path="/forecast" 
element={<Forecast/>}
/>


<Route 
path="/history" 
element={<History/>}
/>


<Route 
path="/about" 
element={<About/>}
/>


<Route 
path="*" 
element={<NotFound/>}
/>


</Routes>

</MainLayout>

</BrowserRouter>

)

}


export default AppRoutes;