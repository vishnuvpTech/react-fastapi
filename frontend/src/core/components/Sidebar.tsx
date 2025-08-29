import { Link } from "react-router-dom";
import { useAuth } from "../../modules/auth/hooks/useAuth";

export default function Sidebar() {
  const { logout } = useAuth();
  return (
    <aside className="w-64 bg-gray-800 text-white h-screen p-4">
      <h2 className="text-xl font-bold mb-6">My App</h2>
      <nav>
        <ul>
          <li className="mb-2"><Link to="/dashboard">Dashboard</Link></li>
        </ul>
      </nav>
      <button
        onClick={logout}
        className="mt-6 bg-red-500 w-full py-2 rounded"
      >
        Logout
      </button>
    </aside>
  );
}
