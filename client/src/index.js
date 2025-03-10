import React from 'react';
import ReactDOM from 'react-dom';

function App() {
  return (
    <div>
      <h1>Welcome to the React Frontend!</h1>
      <p>This is a simple React application bundled as static files.</p>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));
