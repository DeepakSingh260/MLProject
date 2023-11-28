import './App.css';
import Prompt from './Components/prompt';

function App() {
  const heading = "Story GPT";
  return (
    <div className="App">
      
      <h1 style={{textAlign:'center'}}>{heading}</h1>
      <div className="background-image"></div>
      <Prompt/>
    </div>
  );
}

export default App;
