/**
 * AI Agent Chat Interface
 */

import { useState } from 'react';
import Head from 'next/head';
import { agentAPI } from '@/services/api';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  references?: any[];
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const conversationHistory = messages.map((msg) => ({
        role: msg.role,
        content: msg.content,
      }));

      const response = await agentAPI.chat({
        message: input,
        conversation_history: conversationHistory,
      });

      const assistantMessage: Message = {
        role: 'assistant',
        content: response.data.response,
        references: response.data.references,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error:', error);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: 'Sorry, I encountered an error. Please try again.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const quickQuestions = [
    'What crops grow best in Riyadh region?',
    'Recommend livestock for Al-Jouf',
    'Forecast wheat prices for next 6 months',
    'What are the best aquaculture opportunities?',
  ];

  return (
    <>
      <Head>
        <title>AI Agent - RBAT</title>
      </Head>

      <div className="min-h-screen bg-gray-50">
        {/* Header */}
        <header className="bg-saudi-green text-white py-4 shadow-lg">
          <div className="container mx-auto px-6">
            <h1 className="text-2xl font-bold">🤖 Agriculture AI Agent</h1>
            <p className="text-sm text-green-100">
              Ask anything about Saudi Arabian agriculture
            </p>
          </div>
        </header>

        <div className="container mx-auto px-6 py-8 max-w-5xl">
          {/* Welcome Message */}
          {messages.length === 0 && (
            <div className="text-center mb-8">
              <h2 className="text-3xl font-bold mb-4">
                Welcome to RBAT AI Agent
              </h2>
              <p className="text-gray-600 mb-6">
                I can help you with crop recommendations, livestock analysis,
                market forecasts, and more.
              </p>

              <div className="grid md:grid-cols-2 gap-4">
                {quickQuestions.map((question, i) => (
                  <button
                    key={i}
                    onClick={() => setInput(question)}
                    className="bg-white p-4 rounded-lg shadow hover:shadow-md transition text-left"
                  >
                    <span className="text-sm text-gray-700">{question}</span>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Messages */}
          <div className="space-y-4 mb-6">
            {messages.map((message, i) => (
              <div
                key={i}
                className={`flex ${
                  message.role === 'user' ? 'justify-end' : 'justify-start'
                }`}
              >
                <div
                  className={`max-w-3xl rounded-lg p-4 ${
                    message.role === 'user'
                      ? 'bg-saudi-green text-white'
                      : 'bg-white shadow'
                  }`}
                >
                  <div className="prose max-w-none">
                    {message.content.split('\n').map((line, j) => (
                      <p key={j}>{line}</p>
                    ))}
                  </div>

                  {message.references && message.references.length > 0 && (
                    <div className="mt-4 pt-4 border-t border-gray-200">
                      <h4 className="font-semibold text-sm mb-2">
                        References:
                      </h4>
                      <ul className="text-sm space-y-1">
                        {message.references.slice(0, 5).map((ref, j) => (
                          <li key={j} className="text-blue-600">
                            [{ref.id}] {ref.title} ({ref.year})
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              </div>
            ))}

            {loading && (
              <div className="flex justify-start">
                <div className="bg-white rounded-lg p-4 shadow">
                  <div className="flex space-x-2">
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-100"></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-200"></div>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Input Form */}
          <form onSubmit={handleSubmit} className="sticky bottom-0 bg-white rounded-lg shadow-lg p-4">
            <div className="flex space-x-4">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask about crops, livestock, climate, forecasts..."
                className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-saudi-green"
                disabled={loading}
              />
              <button
                type="submit"
                disabled={loading || !input.trim()}
                className="bg-saudi-green text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Send
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  );
}
