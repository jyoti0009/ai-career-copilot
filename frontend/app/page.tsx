
"use client";

import { useState } from "react";

const API = "http://127.0.0.1:8000";

type AnalysisResult = {
  match_percentage: number;
  matching_skills: string[];
  missing_skills: string[];
  skill_gap_count: number;
  recommendations: {
    skill: string;
    recommendation: string;
  }[];
};

export default function Home() {
  const [resume, setResume] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState<AnalysisResult | null>(null);

  async function analyzeResume() {
    setError("");
    setResult(null);

    if (!resume) {
      setError("Please upload your resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please paste the job description.");
      return;
    }

    if (!resume.name.toLowerCase().endsWith(".pdf")) {
      setError("Please select a PDF file.");
      return;
    }

    setLoading(true);

    try {
      // 1. Upload and extract resume skills
      const formData = new FormData();
      formData.append("file", resume);

      const resumeResponse = await fetch(
        `${API}/upload-resume`,
        {
          method: "POST",
          body: formData,
        }
      );

      const resumeData = await resumeResponse.json();

      if (!resumeResponse.ok) {
        throw new Error(
          resumeData.detail || "Resume upload failed."
        );
      }

      // 2. Extract skills required by the job
      const jobResponse = await fetch(`${API}/analyze-job`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          description: jobDescription,
        }),
      });

      const jobData = await jobResponse.json();

      if (!jobResponse.ok) {
        throw new Error(
          jobData.detail || "Job description analysis failed."
        );
      }

      // 3. Calculate resume-job match
      const matchResponse = await fetch(`${API}/match-resume`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          resume_skills: resumeData.skills,
          job_skills: jobData.required_skills,
        }),
      });

      const matchData = await matchResponse.json();

      if (!matchResponse.ok) {
        throw new Error(
          matchData.detail || "Match calculation failed."
        );
      }

      // 4. Generate learning recommendations
      const recommendationResponse = await fetch(
        `${API}/career-recommendations`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            missing_skills: matchData.missing_skills,
          }),
        }
      );

      const recommendationData =
        await recommendationResponse.json();

      if (!recommendationResponse.ok) {
        throw new Error(
          recommendationData.detail ||
            "Could not generate recommendations."
        );
      }

      setResult({
        ...matchData,
        ...recommendationData,
      });
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong. Please try again."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 px-5 py-12 text-white">
      <div className="mx-auto max-w-5xl">
        <header className="text-center">
          <h1 className="text-4xl font-bold">
            AI Career Copilot 🚀
          </h1>
          <p className="mt-3 text-slate-400">
            Discover how well your resume matches a job.
          </p>
        </header>

        <div className="mt-10 grid gap-8 md:grid-cols-2">
          <section className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              📄 Upload Resume
            </h2>
            <p className="mt-2 text-sm text-slate-400">
              Select your resume in PDF format.
            </p>
            <input
              type="file"
              accept=".pdf,application/pdf"
              onChange={(e) =>
                setResume(e.target.files?.[0] || null)
              }
              className="mt-6 block w-full rounded-lg border border-slate-700 bg-slate-800 p-3 text-sm"
            />
            {resume && (
              <p className="mt-3 break-all text-sm text-green-400">
                Selected: {resume.name}
              </p>
            )}
          </section>

          <section className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
            <h2 className="text-xl font-semibold">
              💼 Job Description
            </h2>
            <p className="mt-2 text-sm text-slate-400">
              Paste the job description below.
            </p>
            <textarea
              value={jobDescription}
              onChange={(e) =>
                setJobDescription(e.target.value)
              }
              placeholder="Paste job description here..."
              className="mt-6 h-40 w-full rounded-lg border border-slate-700 bg-slate-800 p-4 text-sm outline-none focus:border-blue-500"
            />
          </section>
        </div>

        <div className="mt-8 text-center">
          <button
            onClick={analyzeResume}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-8 py-3 font-semibold transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Analyzing..." : "🔍 Analyze Resume"}
          </button>
        </div>

        {error && (
          <div
            role="alert"
            className="mt-6 rounded-xl border border-red-700 bg-red-950 p-4 text-red-300"
          >
            {error}
          </div>
        )}

        {result && (
          <section className="mt-10 space-y-6">
            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-8 text-center">
              <p className="text-slate-400">Resume–Job Match</p>
              <p className="mt-2 text-6xl font-bold text-blue-400">
                {result.match_percentage}%
              </p>
              <div className="mx-auto mt-5 h-3 max-w-xl overflow-hidden rounded-full bg-slate-700">
                <div
                  className="h-full rounded-full bg-blue-500"
                  style={{
                    width: `${Math.min(
                      100,
                      Math.max(0, result.match_percentage)
                    )}%`,
                  }}
                />
              </div>
            </div>

            <div className="grid gap-6 md:grid-cols-2">
              <div className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
                <h2 className="text-xl font-semibold text-green-400">
                  ✅ Matching Skills
                </h2>
                {result.matching_skills.length ? (
                  <ul className="mt-4 list-inside list-disc space-y-2">
                    {result.matching_skills.map((skill) => (
                      <li key={skill}>{skill}</li>
                    ))}
                  </ul>
                ) : (
                  <p className="mt-4 text-slate-400">
                    No matching skills detected.
                  </p>
                )}
              </div>

              <div className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
                <h2 className="text-xl font-semibold text-orange-400">
                  📚 Skills to Improve
                </h2>
                {result.missing_skills.length ? (
                  <ul className="mt-4 list-inside list-disc space-y-2">
                    {result.missing_skills.map((skill) => (
                      <li key={skill}>{skill}</li>
                    ))}
                  </ul>
                ) : (
                  <p className="mt-4 text-slate-400">
                    No skill gaps detected by this analysis.
                  </p>
                )}
              </div>
            </div>

            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-6">
              <h2 className="text-xl font-semibold">
                💡 Learning Recommendations
              </h2>
              {result.recommendations.length ? (
                <ul className="mt-4 space-y-4">
                  {result.recommendations.map((item) => (
                    <li
                      key={item.skill}
                      className="rounded-xl bg-slate-800 p-4"
                    >
                      <p className="font-semibold text-blue-300">
                        {item.skill}
                      </p>
                      <p className="mt-1 text-sm text-slate-300">
                        {item.recommendation}
                      </p>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="mt-4 text-slate-400">
                  No recommendations needed for the detected skills.
                </p>
              )}
            </div>
          </section>
        )}
      </div>
    </main>
  );
}
