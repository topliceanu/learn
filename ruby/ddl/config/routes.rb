Rails.application.routes.draw do
  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end

  scope '/accounts/:account_id' do

    # Metrics and Datapoints API.
    post '/metrics', {to: 'metric#create', as: 'create_metric', format: 'json'}
    patch '/metrics/:metric_id', {to: 'metric#update', as: 'update_metric', format: 'json'}
    delete '/metrics/:metric_id', {to: 'metric#remove', as: 'remove_metric', format: 'json'}

    post '/metrics/:metric_id/datapoints', {to: 'metric#add_datapoint', as: 'add_datapoint'}
    get '/metrics/:metric_id/datapoints', {to: 'metric#read_datapoints', as: 'read_datapoints'}

    # Chart API.
    resource :charts

  end

end
