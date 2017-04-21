class ApplicationController < ActionController::Base
	protect_from_forgery with: :exception
	before_filter :configure_permitted_parameters, if: :devise_controller?

	protected

        def configure_permitted_parameters
            devise_parameter_sanitizer.permit(:sign_up) { |u| u.permit(:nombre, :email, :password, :password_confirmation, :username, :nacimiento, :genero) }
            update_attrs = [:password, :password_confirmation, :current_password, :username, :email, :nombre]
    		devise_parameter_sanitizer.permit :account_update, keys: update_attrs
        end
end


