import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "../../modules/auth/hooks/useAuth";

import Login from "../../modules/auth/pages/Login";
import Dashboard from "../../modules/dashboard/pages/Dashboard";
import Layout from "../components/Layout";

function PrivateRoute({ children }: { children: JSX.Element }) {
  const { isAuthenticated } = useAuth();
  return isAuthenticated() ? children : <Navigate to="/login" />;
}

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Layout>
                <Dashboard />
              </Layout>
            </PrivateRoute>
          }
        />

        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>
    </BrowserRouter>
  );
}
