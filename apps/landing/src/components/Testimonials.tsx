import { TestimonialImage } from "../store/constants";

export default function Testimonials(): JSX.Element {
  return (
    <section className="relative">
      <div
        className="absolute left-1/2 transform -translate-x-1/2 bottom-0 pointer-events-none -mb-32"
        aria-hidden="true"
      ></div>

      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">
          <div className="max-w-3xl mx-auto text-center pb-12 md:pb-16">
            <h2 className="h2 mb-4 mt-5">Trusted by over 20,000 companies all over the world</h2>
            <p className="text-xl text-gray-600">
              We are a team of designers and developers who help brands with their digital products.
            </p>
          </div>
          <div className="max-w-3xl mx-auto mt-20">
            <div className="relative flex items-start border-2 border-gray-200 rounded bg-white">
              <div className="text-center px-12 py-8 pt-20 mx-4 md:mx-0">
                <div className="absolute top-0 -mt-8 left-1/2 transform -translate-x-1/2">
                  <img
                    className="relative rounded-full"
                    src={TestimonialImage}
                    width="96"
                    height="96"
                    alt="Testimonial 01"
                  />
                </div>
                <blockquote className="text-xl font-medium mb-4">
                  "I love this product and would recommend it to anyone. Could be not easier to use,
                  and our multiple websites are wonderful. We get nice comments all the time."
                </blockquote>
                <cite className="block font-bold text-lg not-italic mb-1">Arvind</cite>
                <div className="text-gray-600">
                  <span>CEO & Founder </span>
                  <a
                    className="text-blue-600 hover:underline"
                    href="https://arvind11.tk/"
                    target="_blank"
                  >
                    @Arvind
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
