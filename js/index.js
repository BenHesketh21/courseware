function addContent(content) {
    content = content.replace("&gt;", ">")
    document.getElementById('content').innerHTML = marked(content)
}

function enablePrism() {
    let script = document.createElement("script")
    script.src = "/lib/js/prism.js"
    document.body.appendChild(script)
}

function addTopicHeading(topicName) {
    topicHeading = document.createElement("h1")
    topicHeading.innerHTML = topicName
    topicHeading.id = "topic-heading"
    document.getElementById("top-bar").appendChild(topicHeading)
}

function moveModuleHeadingToTopBar() {
    let title = [].filter.call(document.getElementById('content').children, function(el) {
        return el.nodeName === "H1";
    })[0]
    title.remove()
    title.id = "module-heading"
    document.getElementById("top-bar").appendChild(title)
}

function withState(callback) {
    axios.get("/state.json").then((response) => {
        callback(response.data)
    })
}

function getGitUri(topics, resourceName) {
    let gitUri = ""
    topics.forEach((topic) => {
        topic.modules.forEach((module) => {
            if (module.resourceName === resourceName) {
                gitUri = module.gitUri
            }
        })
    })
    return gitUri
}

function getTopicName(state, resourceName) {
    let topic = state.topics.filter((topic)=> {
        return topic.resourceName == resourceName
    })[0]
    return topic.name
}

function getModuleName(state, resourceName) {
    let moduleName = ""
    for (let topic of state.topics) {
        if (!moduleName) {
            for (let module of topic.modules) {
               if (module.resourceName === resourceName) {
                   moduleName = module.name
                   break
               } 
            }
        } else {
            break
        }
    }
    return moduleName
}

function addTableClassToTableElements() {
   let tables = document.getElementsByTagName("TABLE") 
   for (let table of tables) {
        table.className = "table table-bordered"
   }
}

function setTitle(title) {
    document.getElementsByTagName("title")[0].innerHTML = title
}

let resourceName = new URLSearchParams(window.location.search).get("resourceName")

withState((state) => {
    let topicName = getTopicName(state, resourceName.split("/")[0])
    let moduleName = getModuleName(state, resourceName)
    let gitUri = getGitUri(state.topics, resourceName)
    let readme = "/" + gitUri + "/README.md"
    axios.get(readme).then((response) => {
        addContent(response.data)
        enablePrism()
        addTopicHeading(topicName)
        moveModuleHeadingToTopBar()
        addTableClassToTableElements()
        setTitle(topicName + " - " + moduleName)
    })
})

