import './App.css';
import { useState } from 'react';

function Header(props) {
  return <header>
    <h1><a href="/" onClick={(event) => {
      event.preventDefault()
      props.sampleEvent()
    }}>{props.title}</a></h1>
  </header>
}
function Nav(props) {
  // console.log(props)
  const lis = []
  for (let i=0; i<props.topics.length; i++) {
    const t = props.topics[i]
    lis.push(<li key={t.id}><a id={t.id} href={"/read/"+t.id} onClick={(event) => {
      event.preventDefault()
      // console.log(event.target)
      props.sampleEvent(t.id)
      // console.log(typeof(event.target.id))  // string
    }}>{t.title}</a></li>)
  }
  // console.log(lis)
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}
function Article(props) {
  return <article>
  <h2>{props.title}</h2>
  {props.body}
</article>
}
function Create(props) {
  return <article>
    <h2>Create</h2>
    <form onSubmit={e => {
      e.preventDefault()
      const title = e.target.title.value
      const body = e.target.title.value
      props.onCreate(title, body)
    }}>
      <p><input type="text" name="title" placeholder='title'/></p>
      <p><textarea name="body" cols="20" rows="5" placeholder='body'></textarea></p>
      <p><input type="submit" value="Create" /></p>
    </form>
  </article>
}
function Update(props){
  const [title, setTitle] = useState(props.title)
  const [body, setBody] = useState(props.body)
  return <article>
    <h2>Update</h2>
    <form onSubmit={event=>{
      event.preventDefault()
      const title = event.target.title.value
      const body = event.target.body.value
      props.onUpdate(title, body)
    }}>
      <p><input type="text" name="title" placeholder='title' value={title} onChange={event=>{
        setTitle(event.target.value)
      }}/></p>
      <p><textarea name="body" placeholder='body' value={body} onChange={event=>{
        setBody(event.target.body)
      }}></textarea></p>
      <p><input type="submit" value="Update" /></p>
    </form>
  </article>
}
function App() {
  const [mode, setMode] = useState("WELCOME")
  const [id, setId] = useState(null)
  const [nextId, setNextId] = useState(4)
  const [topics, setTopics] = useState([
    {id: 1, title: 'html', body: 'html is ...'},
    {id: 2, title: 'css', body: 'css is ...'},
    {id: 3, title: 'js', body: 'js is ...'},
  ])
  let content = null
  let contextControl = null
  if (mode === "WELCOME") {
    content = <Article title="Welcome" body="Hello, WEB" />
  } else if (mode === "READ") {
    let title, body = null
    for (let i=0; i<topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title
        body = topics[i].body
      }
    }
    content = <Article title={title} body={body} />
    contextControl = <li><a href={`/update/${id}`} onClick={(e) => {
      e.preventDefault()
      setMode("UPDATE")
    }}>Update</a></li>
  } else if (mode === "CREATE") {
    content = <Create onCreate={(title, body) => {
      const newTopic = {id: nextId, title: title, body: body}
      const newTopics = [...topics]
      newTopics.push(newTopic)
      setTopics(newTopics)
      setMode("READ")
      setId(nextId)
      setNextId(nextId + 1)
    }}></Create>
  } else if (mode === 'UPDATE') {
    let title, body = null
    for(let i=0; i<topics.length; i++) {
      if(topics[i].id === id) {
        title = topics[i].title
        body = topics[i].body
      }
    }
    content = <Update title={title} body={body} onUpdate={(title, body) => {
      const newTopics = [...topics]
      const updatedTopic = {id: id, title: title, body: body}
      for (let i =0; i<topics.length; i++) {
        if(newTopics[i].id === id) {
          newTopics[i] = updatedTopic
          break
        }
      }
      setTopics(newTopics)
      setMode("READ")
    }}></Update>
  }
  return (
    <div className="App">
      <Header title="WEB" sampleEvent={() => {setMode("WELCOME")}}/>
      <Nav topics={topics} sampleEvent={(myId) => {
        setMode("READ")
        setId(myId)
      }}/>
      <ul>
        <li>
          <a href="/create" onClick={(e) => {
            e.preventDefault()
            setMode("CREATE")
          }}>CREATE</a>
        </li>
        {contextControl}
      </ul>
      {content}
    </div>
  );
}

export default App;
