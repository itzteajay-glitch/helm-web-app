import React, { useState } from "react";
import axios from "axios";

function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [charts, setCharts] = useState([]);
  const [selectedChart, setSelectedChart] = useState(null);
  const [formData, setFormData] = useState({});
  const [helmYaml, setHelmYaml] = useState("");

  const fetchCharts = async () => {
    const response = await axios.get(`/charts?repo_url=${repoUrl}`);
    setCharts(response.data.charts);
  };

  const fetchChartValues = async (chart) => {
    const response = await axios.get(`/chart/${chart.name}/values?repo_url=${repoUrl}&version=${chart.version}`);
    setSelectedChart(chart);
    setFormData(response.data.values);
  };

  const generateYaml = async () => {
    const payload = {
      name: "my-app",
      namespace: "default",
      chart: selectedChart.name,
      repo: "temp-repo",
      version: selectedChart.version,
      values: formData,
    };
    const response = await axios.post("/generate", payload);
    setHelmYaml(response.data.yaml);
  };

  return (
    <div>
      <h1>Helm Chart Explorer</h1>
      <input
        type="text"
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        placeholder="Enter Helm Repository URL"
      />
      <button onClick={fetchCharts}>Fetch Charts</button>

      {charts.length > 0 && (
        <ul>
          {charts.map((chart) => (
            <li key={chart.name}>
              {chart.name} ({chart.version})
              <button onClick={() => fetchChartValues(chart)}>Select</button>
            </li>
          ))}
        </ul>
      )}

      {formData && (
        <div>
          <h2>Configure Values</h2>
          <button onClick={generateYaml}>Generate YAML</button>
        </div>
      )}

      {helmYaml && (
        <pre>
          <code>{helmYaml}</code>
        </pre>
      )}
    </div>
  );
}

export default App;
