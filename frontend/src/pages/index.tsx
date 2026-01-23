/**
 * RBAT Home Page
 */

import { useState } from 'react';
import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <>
      <Head>
        <title>RBAT - Research-Based Agriculture Technology</title>
        <meta
          name="description"
          content="Intelligent Agriculture Platform for Saudi Arabia"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="min-h-screen bg-gradient-to-b from-green-50 to-white">
        {/* Header */}
        <header className="bg-saudi-green text-white shadow-lg">
          <nav className="container mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <span className="text-3xl">🌾</span>
                <h1 className="text-2xl font-bold">RBAT</h1>
              </div>
              <div className="flex space-x-6">
                <Link href="/dashboard" className="hover:text-saudi-gold transition">
                  Dashboard
                </Link>
                <Link href="/crops" className="hover:text-saudi-gold transition">
                  Crops
                </Link>
                <Link href="/livestock" className="hover:text-saudi-gold transition">
                  Livestock
                </Link>
                <Link href="/fisheries" className="hover:text-saudi-gold transition">
                  Fisheries
                </Link>
                <Link href="/chat" className="hover:text-saudi-gold transition">
                  AI Agent
                </Link>
              </div>
            </div>
          </nav>
        </header>

        {/* Hero Section */}
        <section className="container mx-auto px-6 py-20 text-center">
          <h2 className="text-5xl font-bold text-gray-900 mb-6">
            Intelligence Agriculture for Saudi Arabia
          </h2>
          <p className="text-xl text-gray-600 mb-12 max-w-3xl mx-auto">
            Data-driven insights for crops, livestock, fisheries, and climate.
            Powered by AI with comprehensive references and forecasting.
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
              <div className="text-4xl mb-4">🌱</div>
              <h3 className="text-xl font-semibold mb-2">Crops</h3>
              <p className="text-gray-600">
                Comprehensive crop data, suitability analysis, and recommendations
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
              <div className="text-4xl mb-4">🐄</div>
              <h3 className="text-xl font-semibold mb-2">Livestock</h3>
              <p className="text-gray-600">
                Breed information, farming guides, and profitability analysis
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
              <div className="text-4xl mb-4">🐟</div>
              <h3 className="text-xl font-semibold mb-2">Fisheries</h3>
              <p className="text-gray-600">
                Aquaculture opportunities and fish species suitability
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
              <div className="text-4xl mb-4">🌤️</div>
              <h3 className="text-xl font-semibold mb-2">Climate</h3>
              <p className="text-gray-600">
                Weather data, forecasts, and satellite imagery analysis
              </p>
            </div>
          </div>

          <div className="flex justify-center space-x-4">
            <Link
              href="/chat"
              className="bg-saudi-green text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-700 transition"
            >
              Ask AI Agent
            </Link>
            <Link
              href="/dashboard"
              className="bg-white text-saudi-green border-2 border-saudi-green px-8 py-3 rounded-lg font-semibold hover:bg-green-50 transition"
            >
              View Dashboard
            </Link>
          </div>
        </section>

        {/* Features Section */}
        <section className="bg-white py-20">
          <div className="container mx-auto px-6">
            <h3 className="text-3xl font-bold text-center mb-12">
              Why Choose RBAT?
            </h3>

            <div className="grid md:grid-cols-3 gap-8">
              <div className="text-center">
                <div className="text-5xl mb-4">📚</div>
                <h4 className="text-xl font-semibold mb-3">
                  Referenced Data
                </h4>
                <p className="text-gray-600">
                  All insights backed by verified academic and government sources
                </p>
              </div>

              <div className="text-center">
                <div className="text-5xl mb-4">🤖</div>
                <h4 className="text-xl font-semibold mb-3">
                  AI-Powered Intelligence
                </h4>
                <p className="text-gray-600">
                  Claude AI with RAG for accurate, context-aware recommendations
                </p>
              </div>

              <div className="text-center">
                <div className="text-5xl mb-4">📈</div>
                <h4 className="text-xl font-semibold mb-3">
                  Forecasting & Analytics
                </h4>
                <p className="text-gray-600">
                  Predictive models for yields, prices, and market trends
                </p>
              </div>

              <div className="text-center">
                <div className="text-5xl mb-4">🗺️</div>
                <h4 className="text-xl font-semibold mb-3">
                  Regional Specificity
                </h4>
                <p className="text-gray-600">
                  Tailored insights for all Saudi Arabian regions
                </p>
              </div>

              <div className="text-center">
                <div className="text-5xl mb-4">📊</div>
                <h4 className="text-xl font-semibold mb-3">
                  Comprehensive Reports
                </h4>
                <p className="text-gray-600">
                  Generate detailed reports for research and investment
                </p>
              </div>

              <div className="text-center">
                <div className="text-5xl mb-4">🛰️</div>
                <h4 className="text-xl font-semibold mb-3">
                  Satellite Data
                </h4>
                <p className="text-gray-600">
                  Real-time vegetation indices and soil moisture analysis
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Target Audience */}
        <section className="container mx-auto px-6 py-20">
          <h3 className="text-3xl font-bold text-center mb-12">
            Built For
          </h3>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="bg-gradient-to-br from-green-100 to-green-50 p-6 rounded-lg">
              <h4 className="text-lg font-semibold mb-2">🔬 Researchers</h4>
              <p className="text-gray-700">
                Access comprehensive agricultural data with full references
              </p>
            </div>

            <div className="bg-gradient-to-br from-blue-100 to-blue-50 p-6 rounded-lg">
              <h4 className="text-lg font-semibold mb-2">🚀 Startups</h4>
              <p className="text-gray-700">
                Market analysis and opportunity identification
              </p>
            </div>

            <div className="bg-gradient-to-br from-purple-100 to-purple-50 p-6 rounded-lg">
              <h4 className="text-lg font-semibold mb-2">🎓 Students</h4>
              <p className="text-gray-700">
                Educational resources and case studies
              </p>
            </div>

            <div className="bg-gradient-to-br from-yellow-100 to-yellow-50 p-6 rounded-lg">
              <h4 className="text-lg font-semibold mb-2">💼 Investors</h4>
              <p className="text-gray-700">
                Investment analysis and feasibility studies
              </p>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-gray-900 text-white py-12">
          <div className="container mx-auto px-6 text-center">
            <p className="text-lg mb-4">
              RBAT - Research-Based Agriculture Technology
            </p>
            <p className="text-gray-400">
              Empowering Saudi Arabia's Agricultural Future with AI and Data
            </p>
          </div>
        </footer>
      </div>
    </>
  );
}
