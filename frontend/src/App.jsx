import { useState, useEffect } from "react"

function App() {
  const [activeTab, setActiveTab] = useState("generate")
  const [url, setUrl] = useState("")
  const [loading, setLoading] = useState(false)
  const [quiz, setQuiz] = useState(null)
  const [error, setError] = useState("")

  const [history, setHistory] = useState([])
  const [historyLoading, setHistoryLoading] = useState(false)

  const [selectedQuiz, setSelectedQuiz] = useState(null)
  const [modalOpen, setModalOpen] = useState(false)

  // ---------------- GENERATE QUIZ ----------------
  const generateQuiz = async () => {
    try {
      setError("")
      setLoading(true)

      const encodedUrl = encodeURIComponent(url)

      const response = await fetch(
        `http://127.0.0.1:8000/generate-quiz?url=${encodedUrl}`
      )

      if (!response.ok) throw new Error("Request failed")

      const data = await response.json()
      setQuiz(data)
    } catch{
      setError("Failed to fetch quiz")
    } finally {
      setLoading(false)
    }
  }

  // ---------------- FETCH HISTORY ----------------
  useEffect(() => {
    if (activeTab !== "history") return

    const fetchHistory = async () => {
      try {
        setHistoryLoading(true)
        const res = await fetch("http://127.0.0.1:8000/history")
        const data = await res.json()
        setHistory(data)
      } finally {
        setHistoryLoading(false)
      }
    }

    fetchHistory()
  }, [activeTab])

  // ---------------- FETCH QUIZ DETAILS ----------------
  const openDetails = async (id) => {
    const res = await fetch(`http://127.0.0.1:8000/quiz/${id}`)
    const data = await res.json()
    setSelectedQuiz(data)
    setModalOpen(true)
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-black flex items-center justify-center px-4">
      <div className="bg-gray-900/80 backdrop-blur-lg p-8 rounded-2xl shadow-2xl w-full max-w-5xl border border-gray-700">

        <h1 className="text-3xl font-bold text-white text-center mb-6">
          Wiki Quiz Generator 🧠
        </h1>

        {/* TABS */}
        <div className="flex mb-8 border-b border-gray-700">
          <button
            onClick={() => setActiveTab("generate")}
            className={`px-4 py-2 ${
              activeTab === "generate"
                ? "text-indigo-400 border-b-2 border-indigo-400"
                : "text-gray-400"
            }`}
          >
            Generate Quiz
          </button>

          <button
            onClick={() => setActiveTab("history")}
            className={`ml-6 px-4 py-2 ${
              activeTab === "history"
                ? "text-indigo-400 border-b-2 border-indigo-400"
                : "text-gray-400"
            }`}
          >
            Past Quizzes
          </button>
        </div>

        {/* TAB 1 */}
        {activeTab === "generate" && (
          <>
            <input
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Wikipedia URL"
              className="w-full px-4 py-3 rounded-lg bg-gray-800 text-white mb-4"
            />

            <button
              onClick={generateQuiz}
              disabled={loading}
              className="w-full py-3 bg-indigo-600 rounded-lg text-white"
            >
              {loading ? "Generating..." : "Generate Quiz"}
            </button>

            {error && (
              <p className="text-red-400 text-sm mt-4 text-center">
                {error}
              </p>
            )}

            {quiz && (
              <div className="mt-10 space-y-6">
                <QuizContent quiz={quiz} />
              </div>
            )}
          </>
        )}

        {/* TAB 2 */}
        {activeTab === "history" && (
          <>
            {historyLoading ? (
              <p className="text-gray-400">Loading…</p>
            ) : (
              <table className="w-full text-sm text-gray-300">
                <thead className="bg-gray-800">
                  <tr>
                    <th className="p-2">Title</th>
                    <th className="p-2">URL</th>
                    <th className="p-2">Created</th>
                    <th className="p-2">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {history.map((h) => (
                    <tr key={h.id} className="border-t border-gray-700">
                      <td className="p-2">{h.title}</td>
                      <td className="p-2 truncate">{h.url}</td>
                      <td className="p-2">
                        {new Date(h.created_at).toLocaleDateString()}
                      </td>
                      <td className="p-2">
                        <button
                          onClick={() => openDetails(h.id)}
                          className="text-indigo-400"
                        >
                          Details
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </>
        )}
      </div>

      {/* MODAL */}
      {modalOpen && selectedQuiz && (
        <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50">
          <div className="bg-gray-900 max-w-4xl w-full p-6 rounded-xl overflow-y-auto max-h-[90vh]">
            <div className="flex justify-between mb-4">
              <h2 className="text-xl font-bold text-white">
                {selectedQuiz.title}
              </h2>
              <button
                onClick={() => setModalOpen(false)}
                className="text-gray-400 hover:text-white"
              >
                ✕
              </button>
            </div>

            <QuizContent quiz={selectedQuiz} />
          </div>
        </div>
      )}
    </div>
  )
}

// ---------------- QUIZ CONTENT ----------------
function QuizContent({ quiz }) {
  const difficultyColor = (level) => {
    if (level === "easy") return "bg-green-600"
    if (level === "medium") return "bg-yellow-500"
    if (level === "hard") return "bg-red-600"
    return "bg-gray-500"
  }

  return (
    <>
      {quiz.quiz.map((q, idx) => (
        <div key={idx} className="bg-gray-800 p-5 rounded-xl mb-4">
          <div className="flex justify-between mb-2">
            <p className="text-white font-semibold">
              Q{idx + 1}. {q.question}
            </p>
            <span
              className={`text-xs px-3 py-1 rounded-full text-white ${difficultyColor(
                q.difficulty
              )}`}
            >
              {q.difficulty}
            </span>
          </div>

          <ul className="text-gray-300 text-sm">
            {q.options.map((o, i) => (
              <li key={i}>• {o}</li>
            ))}
          </ul>

          <p className="text-green-400 mt-2">{q.answer}</p>
          <p className="text-gray-400 text-xs">{q.explanation}</p>

          {q.related_topics?.length > 0 && (
            <div className="mt-3">
              <p className="text-xs text-gray-500 mb-1">
                Related topics:
              </p>
              <div className="flex flex-wrap gap-2">
                {q.related_topics.map((t, i) => (
                  <span
                    key={i}
                    className="text-xs bg-gray-700 px-2 py-1 rounded"
                  >
                    {t}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      ))}
    </>
  )
}

export default App
