import { useState } from "react";
import "./App.css";

const API = "http://localhost:8000";

function App() {
  const [brief, setBrief] = useState("");
  const [memories, setMemories] = useState([]);
  const [loading, setLoading] = useState(false);

  const prepareCall = async () => {
    setLoading(true);

    try {
      const [briefRes, memoryRes] = await Promise.all([
        fetch(`${API}/brief`),
        fetch(`${API}/recall`),
      ]);

      const briefData = await briefRes.json();
      const memoryData = await memoryRes.json();

      setBrief(briefData.brief);
      setMemories(memoryData.memories);
    } catch (error) {
      console.error(error);
      alert("Could not connect to DealMind backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <header className="header">
        <div>
          <h1>DealMind</h1>
          <p>AI Sales Deal Intelligence</p>
        </div>

        <div className="memory-badge">
          🧠 Powered by Hindsight
        </div>
      </header>

      <main>

        <section className="hero">
          <div>
            <p className="eyebrow">CUSTOMER INTELLIGENCE</p>
            <h2>Prepare smarter for every sales conversation.</h2>
            <p>
              DealMind remembers customer interactions over time and
              turns them into actionable sales intelligence.
            </p>
          </div>

          <button onClick={prepareCall} disabled={loading}>
            {loading ? "Preparing..." : "Prepare for Next Call →"}
          </button>
        </section>

        <section className="customer-card">
          <div>
            <span>Customer</span>
            <h2>Acme Corp</h2>
          </div>

          <div>
            <span>Memory Status</span>
            <strong>
              🧠 {memories.length || 11} memories recalled
            </strong>
          </div>
        </section>

        <div className="dashboard">

          <section className="panel">
            <div className="panel-title">
              <h2>Customer Memory</h2>
              <span>Hindsight</span>
            </div>

            {memories.length === 0 ? (
              <p className="empty">
                Click "Prepare for Next Call" to recall customer history.
              </p>
            ) : (
              <div className="memory-list">
                {memories.slice(0, 8).map((memory, index) => (
                  <div className="memory" key={index}>
                    <div className="memory-dot"></div>
                    <p>{memory.text}</p>
                  </div>
                ))}
              </div>
            )}
          </section>

          <section className="panel brief-panel">
            <div className="panel-title">
              <h2>AI Call Brief</h2>
              <span>Groq + Hindsight</span>
            </div>

            {!brief ? (
              <div className="empty">
                <div className="big-icon">🤖</div>
                <h3>Your personalized brief will appear here.</h3>
                <p>
                  DealMind will recall Acme Corp's history and prepare
                  the salesperson for the next meeting.
                </p>
              </div>
            ) : (
              <div className="brief">
                {brief.split("\n").map((line, index) => (
                  <p key={index}>{line}</p>
                ))}
              </div>
            )}
          </section>

        </div>

      </main>
    </div>
  );
}

export default App;