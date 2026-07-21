import { useState } from "react";

export default function UploadForm() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!file) {
      alert("Please select a CSV file.");
      return;
    }

    alert(`Selected file: ${file.name}`);

    // Backend API integration will be added later.
  };

  return (
    <div className="card shadow-sm">
      <div className="card-body">
        <h4 className="mb-4">Upload Product Dataset</h4>

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <input
              type="file"
              accept=".csv"
              className="form-control"
              onChange={handleFileChange}
            />
          </div>

          {file && (
            <div className="alert alert-info">
              <strong>Selected:</strong> {file.name}
            </div>
          )}

          <button
            type="submit"
            className="btn btn-primary"
          >
            Upload Dataset
          </button>
        </form>
      </div>
    </div>
  );
}